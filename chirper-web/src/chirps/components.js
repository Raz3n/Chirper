import React, { useState, useEffect } from "react";
import { loadChirps } from "../lookup";

export const ChirpsComponent = (props) => {
  const textAreaRef = React.createRef();
  const [newChirps, setNewChirps] = useState([]);
  const handleSubmit = (event) => {
    event.preventDefault();
    const newVal = textAreaRef.current.value;
    let tempNewChirps = [...newChirps];
    tempNewChirps.unshift({
      content: newVal,
      likes: 0,
      id: 12313,
    });
    setNewChirps(tempNewChirps);
    textAreaRef.current.value = "";
  };
  return (
    <div className={props.className}>
      <div className="col-12 mb-3">
        <form onSubmit={handleSubmit}>
          <textarea
            ref={textAreaRef}
            required={true}
            className="form-control"
            name="chirp"
          ></textarea>
          <button type="submit" className="btn btn-primary my-3">
            Chirp
          </button>
        </form>
      </div>
      <ChirpsList newChirps={newChirps} />
    </div>
  );
};

export const ChirpsList = (props) => {
  const [chirpsInit, setChirpsInit] = useState([]);
  const [chirps, setChirps] = useState([]);
  const [chirpsDidSet, setChirpsDidSet] = useState(false);
  useEffect(() => {
    const final = [...props.newChirps].concat(chirpsInit);
    if (final.length !== chirps.length) {
      setChirps(final);
    }
  }, [props.newChirps, chirps, chirpsInit]);
  useEffect(() => {
    if (chirpsDidSet === false) {
      const myCallback = (response, status) => {
        if (status === 200) {
          setChirpsInit(response);
          setChirpsDidSet(true)
        } else {
          alert("There was an error");
        }
      };
      loadChirps(myCallback);
    }
  }, [chirpsInit, chirpsDidSet, setChirpsDidSet]);
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
  const [likes, setLikes] = useState(chirp.likes ? chirp.likes : 0);
  const [userLike, setUserLike] = useState(
    chirp.userLike === true ? true : false
  );
  const className = props.className
    ? props.className
    : "btn btn-primary btn-sm";
  const actionDisplay = action.display ? action.display : "Action";
  const handleClick = (event) => {
    event.preventDefault();
    if (action.type === "like") {
      if (userLike === true) {
        setLikes(likes - 1);
        setUserLike(false);
      } else {
        setLikes(likes + 1);
        setUserLike(true);
      }
    }
  };
  const display =
    action.type === "like" ? `${likes} ${actionDisplay}` : actionDisplay;
  return (
    <button className={className} onClick={handleClick}>
      {display}
    </button>
  );
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
        <ActionBtn chirp={chirp} action={{ type: "like", display: "Likes" }} />
        <ActionBtn
          chirp={chirp}
          action={{ type: "unlike", display: "Unlike" }}
        />
        <ActionBtn
          chirp={chirp}
          action={{ type: "rechirp", display: "Rechirp" }}
        />
      </div>
    </div>
  );
};
