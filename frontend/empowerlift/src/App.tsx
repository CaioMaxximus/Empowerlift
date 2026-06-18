import { useState, useEffect } from 'react'
import './App.css'
import axios from 'axios'

// class Quote{
//   constructor(quote, author,category){
//     this.quote = quote;
//     this.author = author;
//     this.category  = category;

//   }
// }

function App() {
  const [quote, setQuote] = useState({});
  const api = "http://127.0.0.1:8000/qoutes/"

  useEffect(() =>{
    axios.get(`${api}`).then(res => setQuote(res.data))
    .catch(error => console.log("erro!" , error))}
  ,[]);
  
  return (
    <>
      <div id = "main-quote">
        <h1>{quote.quote}</h1>
        <h2>{quote.author}</h2>
      </div>
      <div id = "banner">
        <h1 id = "first-title"> EMPOWERLIFT</h1><h1 id = "second-title">ME</h1>
      </div>
      
    </>
  )
}

export default App
