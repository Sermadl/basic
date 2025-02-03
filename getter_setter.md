# 자바에서 Getter와 Setter를 사용하는 이유와 간단하게 처리하는 방법

## 1. 자바에서 Getter와 Setter를 사용하는 이유

자바에서 `getter`와 `setter` 메서드를 사용하는 주요 이유는 **캡슐화(encapsulation)** 때문입니다. 캡슐화는 객체 지향 프로그래밍(OOP)의 중요한 원칙 중 하나로, 클래스 내부의 상태(필드)를 외부에서 직접 접근하지 못하도록 숨기고, 이를 제어할 수 있는 메서드를 제공하는 방식입니다. 이를 통해 다음과 같은 이점을 얻을 수 있습니다.

### 1.1. 정보 은닉 (Information Hiding)
- 클래스의 내부 상태를 외부에서 직접 접근할 수 없도록 하여, 객체의 상태가 외부에 의해서 의도치 않게 변경되는 것을 방지할 수 있습니다.
- 필드에 직접 접근하는 대신 `getter`와 `setter`를 통해 안전하게 데이터를 처리합니다.

### 1.2. 데이터 검증
- `setter` 메서드를 사용하여 데이터를 설정할 때 검증을 추가할 수 있습니다. 예를 들어, 음수가 아닌 값을 받아야 한다는 조건을 `setter` 메서드에서 처리할 수 있습니다.

### 1.3. 유연성 및 유지보수
- 필드를 직접 수정하는 대신 메서드를 통해 접근하면, 나중에 필드의 구현을 변경하더라도 외부 코드에서 수정할 필요 없이 메서드만 변경하면 됩니다. 이는 코드의 유지보수를 용이하게 합니다.

### 1.4. 디버깅 및 로깅
- `getter`와 `setter`를 통해 데이터를 접근하고 수정할 때, 디버깅이나 로깅을 추가할 수 있습니다. 예를 들어, 값이 설정될 때마다 로깅을 하거나, 값을 반환할 때 추가적인 로직을 수행할 수 있습니다.

## 2. 간단하게 처리하기 위한 방법

자바에서 `getter`와 `setter`를 일일이 작성하는 것은 반복적인 코드 작성이 많아 불편할 수 있습니다. 이를 간단하게 처리하는 방법으로는 **롬복(Lombok)** 라이브러리를 사용하는 방법이 있습니다. 롬복은 어노테이션을 사용해 `getter`, `setter`, `toString`, `equals` 등을 자동으로 생성해 주는 라이브러리입니다.

### 2.1. Lombok을 사용하여 간단하게 처리하는 방법

#### 1) Lombok 설치
먼저, Lombok을 프로젝트에 추가해야 합니다. Maven 또는 Gradle을 사용하여 Lombok을 의존성에 추가합니다.

- **Maven** 의존성:
```xml
<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <version>1.18.22</version>
    <scope>provided</scope>
</dependency>
```
- **Gradle** 의존성:
```yaml
dependencies {
    compileOnly 'org.projectlombok:lombok:1.18.22'
    annotationProcessor 'org.projectlombok:lombok:1.18.22'
}
```
#### 2) Lombok을 활용한 코드 예시
Lombok을 사용하면 @Getter, @Setter 어노테이션을 클래스 위에 붙여주기만 하면 자동으로 getter와 setter가 생성됩니다.
```java
import lombok.Getter;
import lombok.Setter;

public class Stock {
    @Getter @Setter
    private String ticker; // 주식 종목 코드

    @Getter @Setter
    private String companyName; // 회사 이름

    @Getter @Setter
    private double currentPrice; // 현재 가격

    @Getter @Setter
    private double changePercent; // 변동률 (%)

    @Getter @Setter
    private long volume; // 거래량
}
```
위와 같이 `@Getter`와 `@Setter` 어노테이션을 클래스의 필드에 붙이면, Lombok이 자동으로 각 필드에 대해 `getter`와 `setter` 메서드를 생성합니다. 이렇게 하면 코드가 훨씬 간결해지고, 반복적인 작업을 줄일 수 있습니다.
#### 3) Lombok의 다른 유용한 어노테이션
- `@ToString`: toString() 메서드를 자동으로 생성합니다.
- `@EqualsAndHashCode`: equals() 및 hashCode() 메서드를 자동으로 생성합니다.
- `@NoArgsConstructor`, `@AllArgsConstructor`: 기본 생성자와 모든 필드를 받는 생성자를 자동으로 생성합니다.
## 3. 결론
자바에서 `getter`와 `setter`는 캡슐화의 일환으로 사용되며, 클래스 내부의 상태를 안전하게 관리하고 외부에서 접근할 수 있게 해주는 역할을 합니다. 하지만 이러한 메서드들을 매번 작성하는 것은 번거로울 수 있습니다. 이를 간단히 처리하기 위해 **Lombok** 라이브러리를 활용하면, 코드의 가독성을 높이고 반복적인 작업을 줄일 수 있습니다.