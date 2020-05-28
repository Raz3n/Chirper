import { backendLookup } from "../lookup";

export const apiChirpCreate = (newChirp, callback) => {
  backendLookup("POST", "/chirps/create/", callback, { content: newChirp });
};

export const apiChirpList = (callback) => {
  backendLookup("GET", "/chirps/", callback);
};
