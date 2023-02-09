import { client } from "./client";
import { AccountDTO } from "./dtos/accountDTO";

interface OFXData {
  account: AccountDTO;
}

export async function importFile(file: File): Promise<OFXData> {
  const formData = new FormData();

  formData.append("file", file);

  return client
    .post("/uploadfile", formData, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    })
    .then((data) => {
      return data.data;
    });
}
