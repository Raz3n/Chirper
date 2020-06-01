import React, { useState } from "react";
import { ChirpCreate } from "./create";
import { ChirpsList } from "./list";

export const ChirpsComponent = (props) => {
  const [newChirps, setNewChirps] = useState([]);
  const canChirp = props.canChirp === "false" ? false : true;
  const handleNewChirp = (newChirp) => {
    let tempNewChirps = [...newChirps];
    tempNewChirps.unshift(newChirp);
    setNewChirps(tempNewChirps);
  };
  return (
    <div className={props.className}>
      {canChirp === true && (
        <ChirpCreate didChirp={handleNewChirp} className="col-12 mb-3" />
      )}
      <ChirpsList newChirps={newChirps} {...props} />
    </div>
  );
};
