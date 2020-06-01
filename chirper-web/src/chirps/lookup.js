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

export const apiChirpList = (username, callback) => {
  let endpoint = "/chirps/"
  if (username) {
    endpoint = `/chirps/?username=${username}`
  }
  backendLookup("GET", endpoint, callback);
};
