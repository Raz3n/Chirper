const lookup = (method, endpoint, callback, data) => {
  let jsonData;
  if (data) {
    jsonData = JSON.stringify(data);
  }
  const xhr = new XMLHttpRequest();
  const url = `http://localhost:8000/api${endpoint}`;
  xhr.responseType = "json";
  xhr.open(method, url);
  xhr.onload = () => {
    callback(xhr.response, xhr.status);
  };
  xhr.onerror = () => {
    callback({ message: "The request was an error" }, 400);
  };
  xhr.send(jsonData);
};

export const loadChirps = (callback) => {
  lookup("GET", "/chirps/", callback)
}

