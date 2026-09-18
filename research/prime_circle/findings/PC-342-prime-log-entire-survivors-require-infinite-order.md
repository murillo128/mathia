# PC-342 — prime-log entire survivors require infinite order

**Status:** `EXACT-DERIVED` + `NEGATIVE/OBSTRUCTION` for the full-strip analytic-functional escape left open by PC-341.

PC-341 identifies the exact zero-set threshold for bounded-characteristic interpolation on the native Gamma strip: a function in `N(S_{pi/2})` that vanishes at all but finitely many prime logarithms must vanish identically. That still leaves open the possibility that stronger analytic continuation, by itself, might restore uniqueness even after bounded characteristic is abandoned.

It does not. The prime-log zero set is so dense that every nonzero **entire** function carrying those zeros must have infinite order, but Weierstrass theory also guarantees that such entire functions do exist. They can moreover be chosen even, real on the real axis, and nonnegative there after squaring. Thus full-plane analyticity, reflection symmetry, and reality do not replace the growth hypothesis in PC-341. The residual scalar escape is analytically real, but any entire representative is forced into infinite-order / unbounded-characteristic growth.

## 1. Prime logarithms force infinite order

Let `p_k` be the `k`-th prime and

\[
\lambda_k:=\log p_k.
\tag{1}
\]

Suppose that a nonzero entire function `F` satisfies

\[
F(\lambda_k)=0
\tag{2}
\]

for all but finitely many `k`. If `n_F(r)` denotes the number of zeros of `F` in `|z|\le r`, counted with multiplicity, then

\[
n_F(r)\ge \pi(e^r)-O(1).
\tag{3}
\]

The prime number theorem gives

\[
\pi(e^r)\sim \frac{e^r}{r}.
\tag{4}
\]

On the other hand, if `F` had finite order `rho`, Jensen's formula would imply, for every `epsilon>0`,

\[
n_F(r)=O\!\left(r^{\rho+\epsilon}\right).
\tag{5}
\]

Equations (3)--(5) are incompatible. Hence

\[
\boxed{
F\not\equiv0,\quad F(\log p)=0\text{ for all but finitely many primes }p
\Longrightarrow
\operatorname{ord}F=\infty.
}
\tag{6}
\]

Equivalently, the prime-log zero sequence has infinite exponent of convergence:

\[
\boxed{
\sum_{p}\frac{1}{(\log p)^\alpha}=\infty
\qquad\text{for every }\alpha>0.
}
\tag{7}
\]

Indeed, (7) also follows directly from `p_k\sim k\log k`, since `(\log p_k)^{-\alpha}` is asymptotic to a constant-order multiple of `(\log k)^{-\alpha}`, whose series diverges for every fixed `alpha`.

This rules out, in particular, every finite-order entire repair: exponential-type, Cartwright/Paley-Wiener-type, or any other entire interpolation class whose zero counting is polynomial in the radius cannot support the mixed-semiprime prime-log zero packet.

## 2. Entire survivors nevertheless exist

The obstruction in (6) is a growth obstruction, not an analyticity obstruction. Let

\[
E_m(w):=(1-w)\exp\!\left(w+\frac{w^2}{2}+\cdots+\frac{w^m}{m}\right)
\tag{8}
\]

be the standard Weierstrass primary factor. Define

\[
W(z):=\prod_{k\ge1}
E_k\!\left(\frac{z^2}{\lambda_k^2}\right).
\tag{9}
\]

This product converges locally uniformly. For a fixed compact disk `|z|<=R`, eventually `|z^2/lambda_k^2|<=1/2`, and

\[
\log E_k(w)
=-\sum_{j\ge k+1}\frac{w^j}{j},
\qquad
|\log E_k(w)|\le 2|w|^{k+1}
\tag{10}
\]

there. Since `lambda_k\to\infty`, the tail is dominated after finitely many terms by a geometric series. Therefore `W` is entire. Its only zeros are

\[
z=\pm\lambda_k=\pm\log p_k,
\tag{11}
\]

all simple, and

\[
W(-z)=W(z),
\qquad
W(\bar z)=\overline{W(z)},
\qquad
W(0)=1.
\tag{12}
\]

If nonnegativity on the real axis is also imposed, then

\[
H(z):=W(z)^2
\tag{13}
\]

is a nonzero real entire even function satisfying

\[
H(x)\ge0\quad(x\in\mathbb R),
\qquad
H(\pm\log p)=0
\quad(p\text{ prime}).
\tag{14}
\]

For the Prime-Circle semiprime interpolation attached to a fixed prime shell `p`, one merely omits the factor belonging to that one prime. The resulting entire function is still nonzero, even and real, and vanishes at `log q` for every prime `q\ne p`, exactly the zero packet forced by the mixed-semiprime null condition in PC-339--PC-341.

Thus neither entire continuation nor the elementary reflection/reality symmetries remove the residual zero-set escape.

## 3. Exact relation to the PC-341 boundary

PC-341 proves that a nonzero function in the Nevanlinna class on

\[
S_{\pi/2}=\{z:|\operatorname{Im}z|<\pi/2\}
\tag{15}
\]

cannot have all the prime logarithms as zeros. Consequently every entire survivor constructed above satisfies

\[
\boxed{W\notin N(S_{\pi/2}).}
\tag{16}
\]

Equation (6) shows independently where such a survivor must pay for escaping the PC-341 theorem: it must have infinite entire order. The two statements sharpen the analytic boundary in complementary directions:

- bounded characteristic on the native Gamma strip forces uniqueness, even with arbitrarily large pointwise growth;
- dropping bounded characteristic permits even entire countermodels, but every such countermodel has infinite order because the prime-log zero density is exponential in the Euclidean radius.

So `entire` is not a substitute for `bounded characteristic`, while `finite-order entire` is already too rigid to escape.

## 4. Prior-art and novelty audit

All complex-analysis ingredients are classical. Weierstrass factorization gives an entire function with any prescribed discrete zero set; the relation between exponent of convergence, zero counting, and the order of an entire function is standard Hadamard/Levin theory. A standard reference is B. Ya. Levin, **Distribution of Zeros of Entire Functions**, revised edition, American Mathematical Society, 1980. The prime-counting input in (4) is the classical prime number theorem.

Directed searches for combinations of `prime logarithms`, Weierstrass/canonical products, entire zero sets, and bounded-characteristic/Blaschke uniqueness did not locate an independent zeta or RH mechanism based on this exact prime-log interpolation packet. No historical novelty is claimed for the entire-function construction or for the growth theorem.

The line-local mathematical delta is instead the exact boundary statement left unresolved by PC-341: **full-plane analyticity does not close the out-of-Nevanlinna escape, but the prime-log density forces every entire survivor to have infinite order.** This is a classification/falsification result for the Prime-Circle scalar interpolation mechanism, not a new theorem in entire-function theory.

Because the proof is self-contained and the literature is standard background rather than a load-bearing external identity, no new `SOURCES.md` anchor is required.

## 5. Consequence for the surviving scalar frontier

The scalar global-frequency escape can no longer be justified merely by asking for a stronger domain of holomorphy than the native Gamma strip. Even an entire interpolation function can satisfy every prime-log zero constraint without vanishing, provided one permits sufficiently violent growth.

Conversely, any source-native proposal whose interpolation function is entire of finite order is now ruled out before any RH interpretation is attempted. A genuine remaining candidate must therefore do at least one of the following: produce a source-forced full-strip function outside bounded characteristic; if it is entire, necessarily produce infinite-order growth; or add shell-dependent, nonlinear, matrix-valued, or genuinely cross-shell information beyond the scalar prime-log zero packet.

The Weierstrass survivor itself is **not** evidence for such a candidate. It is an arbitrary analytic interpolant and does not construct a selector `T`, a roots-of-unity operator, a zeta functional equation, a positivity theorem, or a critical-line criterion. Its role is to falsify the stronger uniqueness claim that full-plane analyticity plus natural scalar symmetries would already close the PC-341 escape.

## Audit / falsification tests

The result has four exact checkpoints:

1. the semiprime packet supplies zeros at all but finitely many `log p`, as established in PC-339--PC-341;
2. `pi(e^r)~e^r/r` makes the zero counting exponential in `r`, contradicting finite entire order via Jensen;
3. the variable-genus product (9) must converge locally uniformly and have no zeros beyond `+-log p`;
4. the existence of the entire survivor must not be mistaken for existence of a Prime-Circle selector producing it.

A counterexample to the first half would be a nonzero finite-order entire function vanishing at all but finitely many prime logarithms. A counterexample to the second half would be failure of the locally uniform convergence in (9). Both are excluded by the standard entire-function arguments above.