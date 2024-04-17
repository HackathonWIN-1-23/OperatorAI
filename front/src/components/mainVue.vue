<template>
  <div class="iphone">
    <div class="screen">
      <!-- Notch removed -->
      <div class="phone-content">
        <div class="phone-screen">
          <!-- Input styled to resemble iOS dialer -->
          <input type="text " v-model="phoneNumber" placeholder="Enter number" class="phone-input ios-input">
          <div class="keypad">
            <div class="row">
              <div class="key" @click="addToNumber(1)">1</div>
              <div class="key" @click="addToNumber(2)">2</div>
              <div class="key" @click="addToNumber(3)">3</div>
            </div>
            <div class="row">
              <div class="key" @click="addToNumber(4)">4</div>
              <div class="key" @click="addToNumber(5)">5</div>
              <div class="key" @click="addToNumber(6)">6</div>
            </div>
            <div class="row">
              <div class="key" @click="addToNumber(7)">7</div>
              <div class="key" @click="addToNumber(8)">8</div>
              <div class="key" @click="addToNumber(9)">9</div>

            </div>
            <div class="row">
              <div class="key" @click="addToNumber('+')">+</div>
              <div class="key" @click="addToNumber(0)">0</div>
              <div class="key backspace" @click="removeLastDigit">&#x232b;</div>
              <!-- Call button styled -->
            </div>
            <div class="row">
              <div class="key empty"></div>
              <div class="key empty"></div>
              <div class="key call-btn" @click="makeCall">Call</div>
              <div class="key empty"></div>
              <div class="key empty"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      phoneNumber: ''
    };
  },
  methods: {
    addToNumber(num) {
      this.phoneNumber += num.toString();
    },
    removeLastDigit() {
      this.phoneNumber = this.phoneNumber.slice(0, -1);
    },
    makeCall() {
      if (this.phoneNumber.trim() === '') {
        alert('Please enter a valid phone number.');
      } else {
        // alert('Calling ' + this.phoneNumber);
        window.open('tel:' + this.phoneNumber);
        // Implement your call functionality here
      }
    }
  }
};
</script>

<style scoped>
.iphone {
  //background-color: #fff; /* iPhone background color */
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.screen {
  background-color: #f0f0f0; /* iPhone screen background color */
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.2);
}

.phone-content {
  padding: 20px;
}

.phone-screen {
  background-color: #fff; /* iPhone dialer background color */
  border-radius: 20px;
  padding: 20px;
  display: grid;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
}

.phone-input {
  width: calc(100% - 40px);
  padding: 10px;
  font-size: 18px;
  border: none;
  border-radius: 10px;
  margin-bottom: 20px;
}

/* Additional class for iOS-like input */
.ios-input {
  font-size:28px ;
  font-family: 'San Francisco', Arial, sans-serif; /* Use San Francisco font */
}

.keypad {
  display: grid;
}

.row {
  display: flex;
  justify-content: space-between;

}

.key {
  background-color: #f2f2f2; /* iOS button background color */
  border-radius: 10px;
  padding: 25px;
  margin: 10px 0 10px 0;
  text-align: center;
  font-size: 24px;
  cursor: pointer;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  transition: background-color 0.2s; /* Add transition for press effect */
}

.key.empty {
  visibility: hidden;
  width: 40px ;
}

.key:hover {
  background-color: #e0e0e0; /* Darker shade on hover */
}

/* Styling for call button */
.call-btn {
  background-color: #34c759; /* iPhone call button green */
  color: #fff;
}

.call-btn:hover {
  background-color: #30b454; /* Darker shade on hover */
}

.backspace {
  color: #999;
  font-size: 20px;
}
</style>
