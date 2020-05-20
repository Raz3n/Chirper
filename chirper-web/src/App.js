import React, { useEffect, useState } from "react";
import logo from "./logo.svg";
import "./App.css";

const loadChirps = (callback) => {
  const xhr = new XMLHttpRequest();
  const method = "GET";
  const url = "http://localhost:8000/api/chirps/";
  const responseType = "json";
  xhr.responseType = responseType;
  xhr.open(method, url);
  xhr.onload = () => {
    callback(xhr.response, xhr.status);
  };
  xhr.onerror = () => {
    callback({ message: "The request was an error" }, 400);
  };
  xhr.send();
};

const ActionBtn = (props) => {
  const {chirp, action} = props
  const className = props.className ? props.className : 'btn btn-primary btn-sm'
  return (
    action.type === 'like' ? <button className={className}>{chirp.likes}Likes</button> : null
  );
};

const Chirp = (props) => {
  const { chirp } = props;
  const className = props.className ? props.className : 'col-10 mx-auto col-md-6'
  return (
    <div className={className}>
        <p>{chirp.id} - {chirp.content}</p>
        <div className='btn btn-group'>
          <ActionBtn chirp={chirp} action={{type:"like"}}/>
        </div>
    </div>
  );
};

function App() {
  const [chirps, setChirps] = useState([]);

  useEffect(() => {
    const myCallback = (response, status) => {
      if (status === 200) {
        setChirps(response);
      } else {
        alert("There was an error");
      }
    };
    //do my lookup
    loadChirps(myCallback);
  }, []);
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <div>
          {chirps.map((item, index) => {
            return <Chirp chirp={item} className='my-5 py-5 border bg-white text-dark' key={`${index}-{item.id}`}/>;
          })}
        </div>
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
