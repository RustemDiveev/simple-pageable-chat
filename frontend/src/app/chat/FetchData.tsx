import axios from "axios";

import { CHAT_MESSAGES_URL } from "../../config/api";


const FetchData = () => {

    const fetchData = async () => {
        const result = await axios.get(CHAT_MESSAGES_URL);
        console.log(result);
    }

    return (
        <button onClick={fetchData} children={"Получить сообщения"}/>        
    )
}

export default FetchData;