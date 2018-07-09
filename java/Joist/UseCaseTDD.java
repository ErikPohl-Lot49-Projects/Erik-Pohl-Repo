
import org.junit.Assert;
import org.junit.jupiter.api.Test;


class UseCaseTDD {

	@Test
	void testFirstFibSeq() {
		Assert.assertEquals(1, UseCase.fibonacci(1));
	}
	
	@Test
	void testSecondFibSeq() {
		Assert.assertEquals(1, UseCase.fibonacci(2));
	}
	
	@Test
	void testOutOfBoundsFibSeq() {
		Assert.assertEquals(0, UseCase.fibonacci(-1));
	}
	
	@Test
	void testAddTwoOnes() {
		Assert.assertEquals(1+1, UseCase.add(1,1));
	}
	
	@Test
	void testAddOneAndTwo() {
		Assert.assertEquals(1+2, UseCase.add(1,2));
	}

}
