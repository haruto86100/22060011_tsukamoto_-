import streamlit as st
from logic import fetch_dog_image_by_breed, save_favorite, save_search_history

st.title("🐾 犬種を指定して犬画像を表示")

breed = st.text_input("犬種を英語で入力してください（例: shiba, pug, retriever/golden）")

if st.button("画像を取得"):
    if breed:
        image_url, breed, success = fetch_dog_image_by_breed(breed)
        save_search_history(breed, success)  # 検索履歴に記録

        if success:
            st.image(image_url, caption=f"犬種: {breed}", use_column_width=True)

            if st.button("この画像をお気に入りに保存"):
                save_favorite(image_url, breed)
                st.success("お気に入りに保存しました！")
        else:
            st.error("指定された犬種の画像が見つかりませんでした。")
    else:
        st.warning("犬種を入力してください。")

