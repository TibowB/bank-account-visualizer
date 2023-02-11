import { client } from "./client";
import { AccountDTO } from "./dtos/accountDTO";
import { StatementDTO } from "./dtos/statementDTO";

interface OFXData {
  account: AccountDTO;
  statement: StatementDTO;
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
