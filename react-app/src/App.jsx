import React, { useState } from 'react';

function App() {
  const [count, setCount] = useState(0);
  const retsfg = (
  <div>
    <p>You clicked {count} times.</p>
    <button onClick={() => setCount(count + 1)}>
      Click me dad
    </button>
  </div>);

render(){
  return(
    <div className="App">
      <div className="nav">
        <a>home</a>
        <a>search</a>
        <a>sign in</a>
        <a className="profile" href="#">profile</a>
      </div>
      <div className="main">
        <header className="header">split.box</header>
        <h2>Splitting.... Boxes?</h2>
        <p></p>
        <table>
          <tr>
            <th>What is split.box?</th>
            <th>Why use split.box?</th>
            <th>The Process of using split.box</th>
          </tr>
          <tr>
            <td>
              Split.box is a website facilitating the process of 'splitting boxes'. Suppose you see this really
              nice outfit, however, you only want the shirt. Split.box will allow you to sell the other items, splitting
              up the costs of each item so that you would be able to buy the entire outfit, then send the rest
              of the outfit to the other people who had bought the other parts of the outfit.
            </td>
            <td>
              Unfortunately, most splits occur on social media, either through the means Twitter, Instagram, and Facebook.
              We hope that people will use this website for an easier time for searching for different splits, as well
              as finding people to buy from the seller's splits.
            </td>
            <td>
              <ol>
                <li>Search up items that you desire.</li>
                <li>Choose your desired split</li>
                <li>Request to claim desired item</li>
                <li>Seller will see if your claim is acceptable</li>
                <li>Once the claim was accepted, seller will send a request for payment via whatever they accept </li>
              </ol>
            </td>
          </tr>
        </table>
      </div>
    </div>
  );
}

  return retsfg;
}

export default App;