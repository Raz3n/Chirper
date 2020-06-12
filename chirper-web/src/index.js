import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import {ProfileBadgeComponent} from './profiles'
import {ChirpsComponent, ChirpDetailComponent, FeedComponent} from './chirps'
import * as serviceWorker from './serviceWorker';

const appEl = document.getElementById('root')
if (appEl) {
  ReactDOM.render(<App />, appEl)
}

const e = React.createElement
const chirpsEl = document.getElementById('chirper')
if (chirpsEl) {
  ReactDOM.render(e(ChirpsComponent, chirpsEl.dataset), chirpsEl)
}

const chirpFeedEl = document.getElementById('chirper-feed')
if (chirpFeedEl) {
  ReactDOM.render(e(FeedComponent, chirpFeedEl.dataset), chirpFeedEl)
}

const chirpDetailElements = document.querySelectorAll(".chirper-detail")

chirpDetailElements.forEach(container=> {
  ReactDOM.render(
    e(ChirpDetailComponent, container.dataset), container)
})

const userProfileBadgeElements = document.querySelectorAll(".chirper-2-profile-badge")

userProfileBadgeElements.forEach(container=> {
    ReactDOM.render(
        e(ProfileBadgeComponent, container.dataset), 
        container);
})

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
