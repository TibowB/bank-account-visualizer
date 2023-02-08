import { client } from "./client";

export async function importFile(file: File): Promise<any> {
  const formData = new FormData();

  formData.append("file", file);

  await client.post("/uploadfile", formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });
}
