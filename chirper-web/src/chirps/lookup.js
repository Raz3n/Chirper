import { backendLookup } from "../lookup";

export const apiChirpCreate = (newChirp, callback) => {
  backendLookup("POST", "/chirps/create/", callback, { content: newChirp });
};

export const apiChirpAction = (chirpId, action, callback) => {
  const data = { id: chirpId, action: action };
  backendLookup("POST", "/chirps/action/", callback, data);
};

export const apiChirpDetail = (chirpId, callback) => {
  backendLookup("GET", `/chirps/${chirpId}/`, callback);
};

export const apiChirpFeed = (callback, nextUrl) => {
  let endpoint = "/chirps/feed/";
  if (nextUrl !== null && nextUrl !== undefined) {
    endpoint = nextUrl.replace("http://localhost:8000/api", "")
  }
  backendLookup("GET", endpoint, callback);
};

export const apiChirpList = (username, callback, nextUrl) => {
  let endpoint = "/chirps/";
  if (username) {
    endpoint = `/chirps/?username=${username}`;
  }
  if (nextUrl !== null && nextUrl !== undefined) {
    endpoint = nextUrl.replace("http://localhost:8000/api", "")
  }
  backendLookup("GET", endpoint, callback);
};
