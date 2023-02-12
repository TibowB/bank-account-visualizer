import { AccountDTO } from "./dtos/accountDTO";
import { client } from "./client";

export async function getAccounts(): Promise<AccountDTO[]> {
  return client.get("/account").then((data) => {
    return data.data;
  });
}
