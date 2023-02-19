import { client } from "./client";

export async function importFile(file: File): Promise<string> {
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
