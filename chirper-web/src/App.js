import React, {useEffect, useState} from 'react';
import logo from './logo.svg';
import './App.css';

const loadChirps = (callback) => {
  const xhr = new XMLHttpRequest();
  const method = "GET";
  const url = "http://localhost:8000/api/chirps/";
  const responseType = "json";
  xhr.responseType = responseType;
  xhr.open(method, url);
  xhr.onload = () => {
    callback(xhr.response, xhr.status)
  };
  xhr.onerror = () => {
    callback({"message": "The request was an error"}, 400)
  }
  xhr.send();
};

function App() {
  const [chirps, setChirps] = useState([])
  
  useEffect(() => {
    const myCallback = (response, status) => {
      if (status === 200){
      setChirps(response)
      } else {
        alert("There was an error")
      }
    }
    //do my lookup
    loadChirps(myCallback)
  }, [])
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <p>
          {chirps.map((chirp, index) =>{
          return <li>{chirp.content}</li>
          })}
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
