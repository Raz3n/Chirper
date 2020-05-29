import { backendLookup } from "../lookup";

export const apiChirpCreate = (newChirp, callback) => {
  backendLookup("POST", "/chirps/create/", callback, { content: newChirp });
};

export const apiChirpAction = (chirpId, action, callback) => {
  const data = { id: chirpId, action: action };
  backendLookup("POST", "/chirps/action/", callback, data);
};

export const apiChirpList = (callback) => {
  backendLookup("GET", "/chirps/", callback);
};
