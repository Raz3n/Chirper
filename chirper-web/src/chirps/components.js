import React, { useState, useEffect } from "react";
import { apiChirpAction, apiChirpCreate, apiChirpList } from "./lookup";

export const ChirpsComponent = (props) => {
  const textAreaRef = React.createRef();
  const [newChirps, setNewChirps] = useState([]);

  const handleBackendUpdate = (response, status) => {
    // backend api response handler
    let tempNewChirps = [...newChirps];
    if (status === 201) {
      tempNewChirps.unshift(response);
      setNewChirps(tempNewChirps);
    } else {
      console.log(response);
      alert("An error occured, please try again.");
    }
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    const newVal = textAreaRef.current.value;
    // backend api request handler
    apiChirpCreate(newVal, handleBackendUpdate);
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
      const handleChirpListLookup = (response, status) => {
        if (status === 200) {
          setChirpsInit(response);
          setChirpsDidSet(true);
        } else {
          alert("There was an error");
        }
      };
      apiChirpList(handleChirpListLookup);
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
  const { chirp, action, didPerformAction } = props;
  const likes = chirp.likes ? chirp.likes : 0
  const className = props.className
    ? props.className
    : "btn btn-primary btn-sm";
  const actionDisplay = action.display ? action.display : "Action";

  const handleActionBackendEvent = (response, status) => {
    console.log(response, status);
    if ((status === 200 || status === 201) && didPerformAction) {
      didPerformAction(response, status)
    }
  };
  const handleClick = (event) => {
    event.preventDefault();
    apiChirpAction(chirp.id, action.type, handleActionBackendEvent);
  };
  const display = action.type === "like" ? `${likes} ${actionDisplay}` : actionDisplay;
  return (
    <button className={className} onClick={handleClick}>
      {display}
    </button>
  );
};

export const ParentChirp = (props) => {
  const { chirp } = props;
  return chirp.parent ? 
    <div className="row">
      <div className="col-11 mx-auto p-3 border rounded">
        <p className="mb-0 text-muted small">Rechirp</p>
        <Chirp className={" "} chirp={chirp.parent} />
      </div>
    </div> : null;
};

export const Chirp = (props) => {
  const { chirp } = props;
  const [actionChirp, setActionChirp] = useState(
    props.chirp ? props.chirp : null
  );
  const className = props.className
    ? props.className
    : "col-10 mx-auto col-md-6";

  const handlePerformAction = (newActionChirp, status) => {
    if (status === 200) {
      setActionChirp(newActionChirp)
    } else if (status === 201) {
      //let the chirplist know
    }
  }

  return (
    <div className={className}>
      <div>
        <p>
          {chirp.id} - {chirp.content}
        </p>
        <ParentChirp chirp={chirp} />
      </div>
      {actionChirp && (
        <div className="btn btn-group">
          <ActionBtn
            chirp={actionChirp}
            didPerformAction={handlePerformAction}
            action={{ type: "like", display: "Likes" }}
          />
          <ActionBtn
            chirp={actionChirp}
            didPerformAction={handlePerformAction}
            action={{ type: "unlike", display: "Unlike" }}
          />
          <ActionBtn
            chirp={actionChirp}
            didPerformAction={handlePerformAction}
            action={{ type: "rechirp", display: "Rechirp" }}
          />
        </div>
      )}
    </div>
  );
};
