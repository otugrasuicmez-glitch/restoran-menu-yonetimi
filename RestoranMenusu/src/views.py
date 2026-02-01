import os
import uuid
import pandas as pd
import streamlit as st
import src.database as db
from pathlib import Path, PurePath


# 🔹 Proje kök dizini (RestoranMenusu/)
BASE_DIR = Path(__file__).resolve().parent.parent
IMG_DIR = BASE_DIR / "src" / "img"
IMG_DIR.mkdir(parents=True, exist_ok=True)  # klasör yoksa oluştur


def _resolve_image_path(path_str: str) -> Path:
    """
    DB'den gelen path Windows/Mac/Linux fark etmeksizin düzeltilir
    """
    pure = PurePath(path_str)
    return BASE_DIR / Path(*pure.parts)


def _menu_item_card(menu_item):
    with st.container():
        c1, c2 = st.columns([.3, .7])

        img_path = _resolve_image_path(menu_item["gorsel_yolu"])

        if img_path.exists():
            c1.image(str(img_path))
        else:
            c1.image("https://via.placeholder.com/300x200?text=Gorsel+Yok")

        with c2:
            st.write(f"### {menu_item['isim']}")
            st.write(f"**{menu_item['kategori']}**")
            st.metric("", f"₺{menu_item['fiyat']:.2f}")
            if menu_item["aciklama"]:
                st.text(menu_item["aciklama"])

    st.divider()


def _list_item_card(list_item):
    with st.container():
        c1, c2, c3, c4 = st.columns([1, 5, 2, 1])

        img_path = _resolve_image_path(list_item["gorsel_yolu"])

        if img_path.exists():
            c1.image(str(img_path))
        else:
            c1.image("https://via.placeholder.com/150x100?text=Yok")

        c2.write(f"**{list_item['isim']}**")
        c2.text(list_item["aciklama"])
        c3.text(f"₺{list_item['fiyat']}")

        if c4.button(
            "Sil",
            type="tertiary",
            key=f"sil_{list_item['id']}",
            use_container_width=True
        ):
            db.sil(list_item["id"])
            st.rerun()


def menu_sayfasi():
    st.subheader("Menü", divider=True, text_alignment="center")
    menu = db.menuyu_getir()

    if menu:
        df = pd.DataFrame(
            menu,
            columns=["id", "isim", "aciklama", "kategori", "fiyat", "gorsel_yolu"]
        )
        for _, row in df.iterrows():
            _menu_item_card(row)
    else:
        st.info("Menüde henüz ürün bulunmamaktadır!")


def yonetim_sayfasi():
    st.subheader("Ürün Yönetimi", divider=True, text_alignment="center")

    with st.form("ekle_form", True, enter_to_submit=False):
        c1, c2, c3 = st.columns(3)
        isim = c1.text_input("İsim: *")
        fiyat = c2.number_input("Fiyat: *", min_value=0.0)
        kategori = c3.text_input("Kategori: *")
        gorsel = st.file_uploader("Ürün Görseli: *")
        aciklama = st.text_area("Açıklama:")

        if st.form_submit_button("Ekle", type="primary", use_container_width=True):
            if isim and fiyat and kategori and gorsel:
                ext = Path(gorsel.name).suffix
                img_file = IMG_DIR / f"{uuid.uuid4()}{ext}"

                with open(img_file, "wb") as f:
                    f.write(gorsel.getbuffer())

                # 🔥 DB'ye HER ZAMAN POSIX PATH yaz
                db.ekle(
                    isim,
                    kategori,
                    fiyat,
                    img_file.relative_to(BASE_DIR).as_posix(),
                    aciklama
                )

                st.rerun()
            else:
                st.warning("Lütfen tüm zorunlu alanları doldurun.")

    st.write("**Kayıtlı Ürünler:**")
    menu = db.menuyu_getir()

    if menu:
        df = pd.DataFrame(
            menu,
            columns=["id", "isim", "aciklama", "kategori", "fiyat", "gorsel_yolu"]
        )
        for _, row in df.iterrows():
            _list_item_card(row)
    else:
        st.info("Menüde henüz ürün bulunmamaktadır!")

