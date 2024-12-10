// spotify-api.js // Make sure to rewnew this 
// Load environment variables
require('dotenv').config();

const token = process.env.SPOTIFY_TOKEN;

/**
 * Fetch data from Spotify Web API.
 * @param {string} endpoint - The Spotify API endpoint.
 * @param {string} method - HTTP method (GET, POST, etc.).
 * @param {object} [body] - Optional body for POST requests.
 * @returns {Promise<object>} - The response data from the Spotify API.
 */
async function fetchSpotifyApi(endpoint, method = 'GET', body = null) {
    const res = await fetch(`https://api.spotify.com/v1/${endpoint}`, {
        method: method,
        headers: {
            Authorization: `Bearer ${token}`,
            'Content-Type': 'application/json',
        },
        body: body ? JSON.stringify(body) : null,
    });

    if (!res.ok) {
        throw new Error(`Error: ${res.statusText}`);
    }

    return res.json();
}

/**
 * Get top tracks from the user's Spotify account.
 * @param {number} limit - Number of top tracks to fetch.
 * @returns {Promise<Array>} - An array of top tracks.
 */
async function getTopTracks(limit = 5) {
    const data = await fetchSpotifyApi(`me/top/tracks?limit=${limit}`, 'GET');
    return data.items;
}
