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

  return retsfg;
}

export default App;