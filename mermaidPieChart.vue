<template>
    <div class="container mt-5">
      <div class="card">
        <div class="card-header">
          <h5 class="card-title">과일 분포 파이 차트</h5>
        </div>
        <div class="card-body">
          <div class="mermaid">
            pie
              title 과일 분포
              "사과" : 30
              "배" : 50
              "포도" : 20
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import mermaid from 'mermaid'
  
  export default {
    name: 'MermaidPieChart',
    mounted() {
      // Mermaid 초기화
      mermaid.initialize({ startOnLoad: true })
    },
  }
  </script>
  
  <style scoped>
  /* 필요시 추가 스타일을 작성할 수 있습니다 */
  .mermaid {
    background-color: #f8f9fa;
    padding: 15px;
    border-radius: 5px;
    border: 1px solid #ddd;
  }
  </style>
  