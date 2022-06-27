// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract iot {
  uint[] pressure;
  uint[] wheelNo;

  function addFeed(uint p, uint w) public {
    pressure.push(p);
    wheelNo.push(w);
  }

  function viewFeed() public view returns(uint[] memory, uint[] memory) {
    return (pressure,wheelNo);
  }
}
