import React from "react";
import { apiChirpCreate } from "./lookup";

export const ChirpCreate = (props) => {
  const textAreaRef = React.createRef();
  const { didChirp } = props;
  const handleBackendUpdate = (response, status) => {
    if (status === 201) {
      didChirp(response);
    } else {
      console.log(response);
      alert("An error occured, please try again.");
    }
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    const newVal = textAreaRef.current.value;
    apiChirpCreate(newVal, handleBackendUpdate);
    textAreaRef.current.value = "";
  };
  return (
    <div className={props.className}>
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
  );
};
