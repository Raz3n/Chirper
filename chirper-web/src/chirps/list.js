import React, { useState, useEffect } from "react";
import {apiChirpList } from "./lookup";
import {Chirp} from "./detail"

export const ChirpsList = (props) => {
    const [chirpsInit, setChirpsInit] = useState([]);
    const [chirps, setChirps] = useState([]);
    const [nextUrl, setNextUrl] = useState(null);
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
            setNextUrl(response.next)
            setChirpsInit(response.results);
            setChirpsDidSet(true);
          } else {
            alert("There was an error");
          }
        };
        apiChirpList(props.username, handleChirpListLookup);
      }
    }, [chirpsInit, chirpsDidSet, setChirpsDidSet, props.username]);
  
    const handleDidRechirp = (newChirp) => {
      const updateChirpsInit = [...chirpsInit];
      updateChirpsInit.unshift(newChirp);
      setChirpsInit(updateChirpsInit);
      const updateFinalChirps = [...chirps];
      updateFinalChirps.unshift(chirps);
      setChirps(updateFinalChirps);
    };
    return <React.Fragment> {chirps.map((item, index) => {
      return (
        <Chirp
          chirp={item}
          didRechirp={handleDidRechirp}
          className="my-5 py-5 border bg-white text-dark"
          key={`${index}-{item.id}`}
        />
    )})}
    { nextUrl !== null && <button className='btn btn-outline-primary'>Load Next</button>}
    </React.Fragment>
  };