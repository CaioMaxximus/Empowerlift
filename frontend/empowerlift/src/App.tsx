import { useState, useEffect } from 'react'
import './App.css'
import axios from 'axios'


function App() {
  const [quoteRes, setQuoteRes] = useState(null);
  const api = "http://127.0.0.1:8000/quotes/"

  useEffect(() =>{
    axios.get(`${api}`).then(res => setQuoteRes(res.data))
    .catch(error => console.log("erro!" , error))}
  ,[]);

  if (!quoteRes) {
    console.log("nao carreguei ainda")
    return <div>Carregando...</div>;
  }
  console.log(quoteRes)
  let my_quote = quoteRes.quote.quote;
  let author = quoteRes.quote.author;
  let image_url = quoteRes.photo.urls.full;

  
  return (
    <>
      {/* <div className='backgrond-div'> */}
        <img src={image_url} alt="" className = "background-img"/>
      {/* </div> */}
      <div id = "main-quote">
        <h1>{my_quote}</h1>
        <h2>{author}</h2>
      </div>
      <div id = "banner">
        <h1 id = "first-title"> EMPOWERLIFT</h1><h1 id = "second-title">ME</h1>
      </div>
      
    </>
  )
}

export default App
