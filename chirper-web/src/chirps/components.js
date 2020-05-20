import React, {useState, useEffect} from "react";
import {loadChirps} from "../lookup"

export const ChirpsList = (props) => {
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
  return chirps.map((item, index) => {
    return (
      <Chirp
        chirp={item}
        className="my-5 py-5 border bg-white text-dark"
        key={`${index}-{item.id}`}
      />
    );
  });
};

export const ActionBtn = (props) => {
  const { chirp, action } = props;
  const className = props.className
    ? props.className
    : "btn btn-primary btn-sm";
  return action.type === "like" ? (
    <button className={className}>{chirp.likes}Likes</button>
  ) : null;
};

export const Chirp = (props) => {
  const { chirp } = props;
  const className = props.className
    ? props.className
    : "col-10 mx-auto col-md-6";
  return (
    <div className={className}>
      <p>
        {chirp.id} - {chirp.content}
      </p>
      <div className="btn btn-group">
        <ActionBtn chirp={chirp} action={{ type: "like" }} />
        <ActionBtn chirp={chirp} action={{ type: "like" }} />
      </div>
    </div>
  );
};
