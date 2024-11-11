// homepage.js

/**
 * Update the DOM with the user's top albums.
 * @param {Array} tracks - Array of track objects from Spotify.
 */
function updateTopAlbums(tracks) {
    const albumList = document.getElementById('album-list');
    
    // Keep track of added albums to avoid duplicates
    const addedAlbums = new Set();

    tracks.forEach(track => {
        const album = track.album;

        // Check if the album has already been added to avoid duplicates
        if (!addedAlbums.has(album.id)) {
            // Create album card element
            const albumItem = document.createElement('div');
            albumItem.classList.add('playlist-info');

            albumItem.innerHTML = `
                <img src="${album.images[0].url}" alt="Album Cover" class="playlist-image">
                <div class="playlist-details">
                    <h3>Album</h3>
                    <h1 class="playlist-title">${album.name}</h1>
                    <p>${album.artists[0].name} - ${album.release_date}</p>
                    <div class="playlist-actions">
                        <button class="play-btn">Play</button>
                        <button class="follow-btn">Follow</button>
                    </div>
                </div>
            `;

            // Append the album card to the album list
            albumList.appendChild(albumItem);
            addedAlbums.add(album.id); // Mark album as added
        }
    });
}

// Fetch the user's top tracks and update the DOM
getTopTracks(5)
    .then(tracks => {
        updateTopAlbums(tracks);
    })
    .catch(error => {
        console.error('Error fetching albums:', error);
    });
