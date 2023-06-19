import streamlit as st
from pytube import YouTube

def download_video(url, save_path):
    try:
        # Create a YouTube object with the video URL
        youtube = YouTube(url)

        # Get the highest resolution progressive video
        video = youtube.streams.get_highest_resolution()

        # Download the video to the specified save path
        video.download(save_path)

        st.success("Video downloaded successfully!")

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

def main():
    st.title("YouTube Video Downloader")

    # User input: YouTube video URL
    video_url = st.text_input("Enter YouTube video URL:")

    # User input: Save location
    save_location = st.text_input("Enter save location:")

    # Download button
    if st.button("Download"):
        if video_url and save_location:
            download_video(video_url, save_location)
        else:
            st.warning("Please enter a video URL and save location.")

if __name__ == "__main__":
    main()
