package UnusedLibrary //this will not compile because "fmt" is not used

import (
"fmt"
)

func UnusedLibraryFunction(n string) (UnusedLibraryFunctionReturn string) {
	n = n + " unused fmt package"
	return n
}
