from dataclasses import dataclass
from typing import Optional
from pydantic import TypeAdapter

@dataclass
class Address:
    location: str
    country: str

@dataclass
class Person:
    name: str
    address: Address
    age: Optional[int] = None

def main():
    with open("persons.json") as f:
        data = f.read()

    persons = TypeAdapter(list[Person]).validate_json(data)

    for person in persons:
        print(f"{person.name} from {person.address.location}", end=" ")
        if person.age:
            print(f"is {person.age} years old")
        else:
            print("does not want to disclose its age")

    data = TypeAdapter(list[Person]).dump_json(persons, indent=2, exclude_none=True)
    # we have to use decode otherwise print prints the string representation of the bytes
    # or sys.stdout.write(data) would be the alternative
    print(data.decode())

if __name__ == "__main__":
    main()
