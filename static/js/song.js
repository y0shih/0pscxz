/**
 * Update the DOM with dynamically fetched songs.
 * @param {Array} tracks - The top tracks fetched from the Spotify API.
 */
function displayTracks(tracks) {
    const mainContent = document.querySelector('.playlist-section');
    mainContent.innerHTML = '';  // Clear the existing content

    tracks.forEach(track => {
        const album = track.album;
        const artist = track.artists.map(artist => artist.name).join(', ');

        // Create a new section for each track
        const playlistBanner = document.createElement('section');
        playlistBanner.classList.add('playlist-banner');

        // Create the playlist info
        const playlistInfo = document.createElement('div');
        playlistInfo.classList.add('playlist-info');

        playlistInfo.innerHTML = `
            <img src="${album.images[0].url}" alt="Album Cover" class="playlist-image">
            <div class="playlist-details">
                <span class="playlist-type">Album</span>
                <h1 class="playlist-title">${album.name}</h1>
                <div class="playlist-meta">
                    <span class="artist-name">${artist}</span>
                    <span>${album.release_date.substring(0, 4)}</span>
                    <span>${album.total_tracks} Songs</span>
                </div>
                <div class="playlist-actions">
                    <button class="play-btn">Play</button>
                    <button class="follow-btn">Follow</button>
                    <button class="more-options">...</button>
                </div>
            </div>
        `;

        // Append the playlist info to the playlist banner section
        playlistBanner.appendChild(playlistInfo);

        // Append the generated content to the main content section (vertically)
        mainContent.appendChild(playlistBanner);
    });
}

// Fetch top tracks and display them
getTopTracks(5)
    .then(tracks => {
        displayTracks(tracks);
    })
    .catch(err => {
        console.error('Error fetching top tracks:', err);
    });
