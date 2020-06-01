import React, { useState } from "react";
import {ActionBtn} from "./buttons"

export const ParentChirp = (props) => {
    const { chirp } = props;
    return chirp.parent ? (
      <div className="row">
        <div className="col-11 mx-auto p-3 border rounded">
          <p className="mb-0 text-muted small">Rechirp</p>
          <Chirp hideActions className={" "} chirp={chirp.parent} />
        </div>
      </div>
    ) : null;
  };
  
  export const Chirp = (props) => {
    const { chirp, didRechirp, hideActions } = props;
    const [actionChirp, setActionChirp] = useState(
      props.chirp ? props.chirp : null
    );
    const className = props.className
      ? props.className
      : "col-10 mx-auto col-md-6";
  
    const handlePerformAction = (newActionChirp, status) => {
      if (status === 200) {
        setActionChirp(newActionChirp);
      } else if (status === 201) {
        if (didRechirp) {
          didRechirp(newActionChirp);
        }
      }
    };
  
    return (
      <div className={className}>
        <div>
          <p>
            {chirp.id} - {chirp.content}
          </p>
          <ParentChirp chirp={chirp} />
        </div>
        {actionChirp && hideActions !== SVGComponentTransferFunctionElement && (
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