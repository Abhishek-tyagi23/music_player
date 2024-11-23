import mysql.connector
from mysql.connector import Error
import os
from pathlib import Path

AUDIO_FOLDER = r'C:\Users\visha\Desktop\Music_player\Home\music\static\music\audio_files'
TITLE_FOLDER = r'C:\Users\visha\Desktop\Music_player\Home\music\static\music\title'
ARTIST_FOLDER = r'C:\Users\visha\Desktop\Music_player\Home\music\static\music\artists' 
THUMBNAIL_FOLDER = r'C:\Users\visha\Desktop\Music_player\Home\music\static\music\thumbnails'



def create_connection():
    """Create and return a connection to the MySQL database."""
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='Abhishek',
            password='2138433',
            database='video'
        )
        if connection.is_connected():
            print("Connected to MySQL database")
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None


def insert_card_data(connection, title_file, artist_files, audio_file, thumbnail_file):
    """Insert a new card entry into the database."""
    cursor = connection.cursor()

    try:
        # Read the title from the .txt file
        with open(title_file, 'r') as f:
            title = f.read().strip()

        # Combine the artist names from all artist files or fallback to 'Unknown Artist'
        with open(artist_files, 'r') as f:
            artist = f.read().strip()
            
       
        # Prepare file paths for audio and thumbnail
        audio_path = f"audio_files/{os.path.basename(audio_file)}"
        thumbnail_path = f"thumbnails/{os.path.basename(thumbnail_file)}"

        # Debugging: print values to be inserted
        print(f"Title: {title}, Artist(s): {artist}, Audio Path: {audio_path}, Thumbnail Path: {thumbnail_path}")

        # Insert the card data into the table
        cursor.execute("""
            INSERT INTO card (title, artist, audio, thumbnail)
            VALUES (%s, %s, %s, %s)
        """, (title, artist, audio_path, thumbnail_path))

        # Commit the transaction
        connection.commit()

        if cursor.rowcount > 0:
            print(f"Successfully inserted card: {title} by {artist}")
        else:
            print(f"No rows inserted for {title} by {artist}")

    except mysql.connector.Error as e:
        print(f"Error inserting data for {title} by {artist}: {e}")
        connection.rollback()
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        cursor.close()


def process_files():
    """Loop through the files and insert them into the database."""
    connection = create_connection()

    if not connection:
        print("Failed to connect to database.")
        return

    # Check if AUDIO_FOLDER exists and contains files
    if not Path(AUDIO_FOLDER).exists():
        print(f"The folder {AUDIO_FOLDER} does not exist.")
        connection.close()
        return
    
    # Get list of audio files
    audio_files = [f for f in os.listdir(AUDIO_FOLDER) if f.lower().endswith('.mp3')]
    
    # Get title, artist, and thumbnail files
    title_files = {os.path.splitext(f)[0]: f for f in os.listdir(TITLE_FOLDER) if f.endswith('.txt')}
    artist_files_dict = {os.path.splitext(f)[0]: f for f in os.listdir(ARTIST_FOLDER) if f.endswith('.txt')}
    thumbnail_files = {os.path.splitext(f)[0]: f for f in os.listdir(THUMBNAIL_FOLDER) if f.endswith('.jpg')}
    
    # Debugging: Print the files found in each folder
    print(f"Found {len(audio_files)} audio files")
    print(f"Found {len(title_files)} title files: {list(title_files.keys())}")
    print(f"Found {len(artist_files_dict)} artist files: {list(artist_files_dict.keys())}")
    print(f"Found {len(thumbnail_files)} thumbnail files: {list(thumbnail_files.keys())}")

    # Loop through each audio file and find corresponding title, artist, and thumbnail
    for audio_file in audio_files:
        base_name = os.path.splitext(audio_file)[0]

        # Check if the corresponding files exist
        title_file = title_files.get(base_name)
        artist_files = artist_files_dict.get(base_name)
        thumbnail_file = thumbnail_files.get(base_name)

        # Debugging: Print what files are being matched
        print(f"Checking {base_name}: Title File: {title_file}, Artist Files: {artist_files}, Thumbnail File: {thumbnail_file}")

        if title_file and artist_files and thumbnail_file:
            # Paths to the actual files
            title_path = Path(TITLE_FOLDER) / title_file
            artist_files = Path(ARTIST_FOLDER) / artist_files
            thumbnail_path = Path(THUMBNAIL_FOLDER) / thumbnail_file

            # Debugging: confirm file paths
            print(f"Processing {base_name}: Title File: {title_path}, Artist Files: {artist_files}, Thumbnail File: {thumbnail_path}")

            # Insert the data into the database
            insert_card_data(connection, title_path, artist_files, audio_file, thumbnail_path)
        else:
            # Add more information about missing files
            missing_files = []
            if not title_file:
                missing_files.append('Title')
            if not artist_files:
                missing_files.append('Artist')
            if not thumbnail_file:
                missing_files.append('Thumbnail')

            print(f"Skipping {base_name} - Missing files: {', '.join(missing_files)}")

    # Ensure the connection is closed
    connection.close()
    print("Database connection closed.")




if __name__ == "__main__":
    process_files()
