import React, {useState, useEffect} from 'react';
import './App.css';
import axios from 'axios';

function App() {
const [list, setList] = useState([]);
const [NewFood, setNewFood] = useState();

async function fetchData() {
  let foodData = await axios.get('http://127.0.0.1:5000/api/food')
  setList(foodData.data)
}

function submitFormData(e) {
  axios.post('http://127.0.0.1:5000/api/food', {
    name: NewFood
  })
  .catch(function (error) {
    console.log(error);
  });
}

useEffect(() => {
  fetchData()
}, [])

function deleteEntry(e) {
  let id = e.target.parentElement.id
  axios.delete(`http://127.0.0.1:5000/api/food/${id}`)
  .catch(function (error) {
    console.log(error);
  });

}

function foodListFunction() {
  console.log(list)
  return list.map(item => (
    <section id={item.id} key={item.id} className="d-flex flex-row m-1">
    <div className="mx-1">{item.id}: </div>
    <div className="mx-1">{item.name}</div>
    <button className="btn btn-warning btn-sm">🖊</button>
    <button className="mx-1 btn btn-danger btn-sm" onClick={deleteEntry}>X</button>
    </section>
  ))
}
  return (
    <section className="container d-flex flex-column text-center align-items-center py-2">
    <h1>Foods we like</h1>
    <section className="card container w-50">
<form onSubmit={submitFormData} className="flex-column">
<h3>Add a food!</h3>
<input type="text" className="form-control mb-2" placeholder="Add a food!" onChange={(e) => setNewFood(e.target.value)}></input>
<button className="form-control btn btn-secondary btn-sm mb-2">Add a new food</button>
</form>
    </section>



    <h3>Food list</h3>
    {foodListFunction()}
    </section>
  );
}

export default App;
