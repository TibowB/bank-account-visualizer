import { AccountDTO } from "./dtos/accountDTO";
import { client } from "./client";

export interface FastApiResponse {
  __data__: AccountDTO;
}

export async function getAccounts(): Promise<AccountDTO[]> {
  return client.get("/account").then((data) => {
    return data.data;
  });
}

export async function addAccount(
  account: AccountDTO
): Promise<FastApiResponse> {
  return client.post("/account", account).then((data) => {
    return data.data;
  });
}
