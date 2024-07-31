import React from 'react';
import './Modal.css';

const Modal = ({ show, handleClose, secretFighter }) => {
    const showHideClassName = show ? "modal display-block" : "modal display-none";

    console.log('Modal Secret Fighter:', secretFighter); // Debugging log

    return (
        <div className={showHideClassName}>
            <section className="modal-main">
                <h2>Secret Fighter Revealed!</h2>
                {secretFighter && (
                    <>
                        <p><strong>{secretFighter.fname} {secretFighter.lname}</strong></p>
                        <p>Nickname: {secretFighter.nickname}</p>
                        <p>Rank: {secretFighter.rank}</p>
                        <p>Division: {secretFighter.division}</p>
                        <p>Style: {secretFighter.style}</p>
                        <p>Country: {secretFighter.country}</p>
                        <p>Debut: {secretFighter.debut}</p>
                    </>
                )}
                <button onClick={handleClose}>Close</button>
            </section>
        </div>
    );
};

export default Modal;
