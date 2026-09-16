# PC-320 — canonical Mordell–Tornheim off-critical zeros form a local hypersurface

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-BOUNDARY` for the full multivariable zero-divisor escape left open by PC-319.

PC-319 proves that the canonical Prime-Circle pair `(q,r)=(5,7)` has zeros with `Re(s)>1` for every sufficiently small positive Mordell–Tornheim coupling `u`, after fixing one real `T>1` in the second Mellin variable. That rules out coordinatewise Riemann-line confinement near the decoupled face, but it deliberately leaves open whether the **full three-variable divisor** could acquire a more selective multivariable interpretation.

The local analytic geometry is stronger than the fixed-slice statement. Around any PC-319 zero `(s_0,T,0)` of the decoupled face, the canonical function is jointly holomorphic in `(s,t,u)`, and Weierstrass preparation in the `s` variable shows that its zero set is a genuine complex-analytic hypersurface, finite of positive degree over an open bidisk of `(t,u)` parameters. Shrinking the neighborhood if necessary, **every point of that parameter bidisk has at least one zero with `Re(s)>1`**. Hence the off-critical phenomenon occupies a two-complex-dimensional local divisor; it is not a defect of one frozen `t=T` slice or of taking `u` real.

Multiplication by any holomorphic completion factor that is nonzero in this neighborhood leaves this divisor unchanged. A local biholomorphic mixing of the Mellin coordinates can only relabel the same hypersurface, not turn it into an isolated spectrum. Therefore a viable multivariable continuation of the PC-316 route must add an independently source-forced selection rule—such as a distinguished submanifold or a nontrivial divisor relation—not merely complete the function by nonvanishing gamma/exponential factors or change coordinates.

## 1. Canonical input from PC-319

Use the canonical Prime-Circle sources at levels `5` and `7`, with periodic Fourier packets `a_5(k)` and `b_7(l)`. PC-316 defines

\[
Z(s,t,u)
:=\sum_{k,l\ge1}
\frac{a_5(k)b_7(l)}{k^s l^t(k+l)^u}.
\tag{1}
\]

PC-319 establishes three facts that are load-bearing here:

1. the one-level periodic Dirichlet series

\[
A_5(s):=\sum_{k\ge1}\frac{a_5(k)}{k^s}
\tag{2}
\]

has a zero `s_0` with

\[
\Re s_0>1;
\tag{3}
\]

2. there exists a real `T>1` for which

\[
B_7(T)\neq0,
\qquad
B_7(t):=\sum_{l\ge1}\frac{b_7(l)}{l^t};
\tag{4}
\]

3. on the decoupled face,

\[
\boxed{Z(s,t,0)=A_5(s)B_7(t).}
\tag{5}
\]

The existence of `s_0` is the only literature-dependent input: PC-319 verifies that `A_5` lies outside the exceptional `P(s)L(s,chi)` class and then applies the Saias–Weingartner zero theorem for periodic Dirichlet series. The present finding adds no stronger one-variable zero theorem.

Let `m>=1` be the multiplicity of `s_0` as a zero of `A_5`.

## 2. The three-variable series is holomorphic across the face `u=0`

The point `u=0` is not a singular boundary of (1). Choose `delta>0` so small that

\[
\Re s_0-2\delta>1,
\qquad
T-2\delta>1.
\tag{6}
\]

Consider a polydisk on which

\[
\Re s>\Re s_0-\delta,
\qquad
\Re t>T-\delta,
\qquad
|\Re u|<\delta.
\tag{7}
\]

The source coefficients are bounded. For `|Re(u)|<delta`,

\[
|(k+l)^{-u}|\le (k+l)^\delta
\le C_\delta(k^\delta+l^\delta),
\tag{8}
\]

so each term in (1) is dominated by a constant multiple of

\[
k^{-\Re s+\delta}l^{-\Re t}
+
k^{-\Re s}l^{-\Re t+\delta}.
\tag{9}
\]

Both double sums converge uniformly on compact subsets by (6)--(7). Hence the defining series converges normally in a full complex neighborhood of `(s_0,T,0)` and therefore

\[
\boxed{Z(s,t,u)\text{ is jointly holomorphic near }(s_0,T,0).}
\tag{10}
\]

This matters because the coupled side `u>0`, the decoupled face `u=0`, and a small complex neighborhood on the other side are one analytic germ. No meromorphic continuation is needed for the argument.

## 3. Weierstrass preparation forces a positive-dimensional zero divisor

At the base point, (5) gives

\[
Z(s_0,T,0)=0.
\tag{11}
\]

Moreover, because `B_7(T)\neq0` and `s_0` has multiplicity `m`,

\[
\partial_s^j Z(s_0,T,0)=0
\quad(0\le j<m),
\qquad
\partial_s^m Z(s_0,T,0)\neq0.
\tag{12}
\]

Apply the Weierstrass preparation theorem to the holomorphic germ (10), taking `s-s_0` as the distinguished variable and `(t-T,u)` as parameters. After shrinking to a polydisk

\[
D_s\times D_t\times D_u
\ni(s_0,T,0),
\tag{13}
\]

there are a nowhere-zero holomorphic unit `U` and holomorphic functions `c_0,...,c_{m-1}` on `D_t\times D_u`, all vanishing at `(T,0)`, such that

\[
\boxed{
Z(s,t,u)
=U(s,t,u)
\left[(s-s_0)^m+
\sum_{j=0}^{m-1}c_j(t,u)(s-s_0)^j\right].
}
\tag{14}
\]

Shrink `D_s` once more so that its closure lies in `Re(s)>1`. Continuity of the roots of the monic polynomial in (14), equivalently the argument principle on `partial D_s`, then gives

\[
\boxed{
N_{D_s}\bigl(Z(\cdot,t,u)\bigr)=m
\quad\text{for every }(t,u)\in D_t\times D_u,
}
\tag{15}
\]

counting multiplicity.

Thus

\[
\mathcal V:=\{(s,t,u):Z(s,t,u)=0\}
\cap(D_s\times D_t\times D_u)
\tag{16}
\]

is a nonempty complex-analytic hypersurface, and the projection

\[
\mathcal V\longrightarrow D_t\times D_u
\tag{17}
\]

is locally a finite branched cover of degree `m`. In particular, **for every sufficiently small complex perturbation of both `t` and `u`, at least one canonical zero remains in `Re(s)>1`.** PC-319's real ray `t=T`, `0<u<epsilon` is only one one-dimensional trace through this divisor.

No simplicity assumption on `s_0` is used. If `m=1`, the implicit-function theorem sharpens (14) to a single holomorphic branch `s=s(t,u)`; for higher multiplicity the Weierstrass polynomial is the correct invariant statement.

## 4. Ordinary completion cannot remove the divisor

Let `C(s,t,u)` be holomorphic and nowhere zero on the polydisk (13). A completion of the form

\[
\Lambda(s,t,u):=C(s,t,u)Z(s,t,u)
\tag{18}
\]

has exactly the same local zero set:

\[
\boxed{\{\Lambda=0\}=\{Z=0\}\quad\text{inside the polydisk}.}
\tag{19}
\]

Consequently gamma factors, powers of `pi`, exponentials, conductor powers, or other standard completion factors that are regular and nonvanishing at this absolute-convergence point cannot repair the PC-319 obstruction. To cancel the divisor one would have to introduce a factor with a pole on precisely the source-specific zero hypersurface, which is extra structure rather than a completion forced by the current geometry.

Likewise, a local biholomorphic coordinate change

\[
(s,t,u)\longmapsto(w_1,w_2,w_3)
\tag{20}
\]

maps `\mathcal V` to another complex-analytic hypersurface. It may straighten or relabel that hypersurface, but it cannot remove it or make the zero set discrete. Therefore an apparent “critical hyperplane” produced only after an arbitrary coordinate choice would be a coordinate gauge unless that choice is independently forced by the Prime-Circle geometry and tied to the RH target by a separate theorem.

This is deliberately narrower than claiming that no mixed-variable RH criterion can exist. A distinguished source-forced submanifold could avoid this local divisor, or a genuinely new relation between several components could select a different zero set. What fails is the idea that the *existing* three-variable divisor becomes Riemann-like merely by standard completion or reparameterization.

## 5. Prior-art and novelty audit

The analytic tools are classical. Weierstrass preparation is standard several-complex-variables theory: a holomorphic germ regular of order `m` in one variable is a nonvanishing unit times a monic degree-`m` polynomial in that variable with holomorphic parameter-dependent coefficients. The consequence that a zero of a holomorphic function of several variables sits in a local analytic hypersurface is likewise standard. No novelty is claimed for these facts.

The destination family is also classical. PC-316 already identifies (1) as a finite character-weighted Mordell–Tornheim `L`-bundle and records Tsumura's functional-relation theory and neighboring Mordell–Tornheim/Witten several-variable literature. PC-319 records the Saias–Weingartner theorem used to obtain the load-bearing absolute-convergence zero of `A_5`.

A directed literature check found the expected several-variable Mordell–Tornheim/Witten analytic continuation and functional-relation literature, and the standard Weierstrass-preparation description of local zero sets. It did not identify a source claiming that the canonical Prime-Circle `(5,7)` coefficient packet has the specific local divisor (16)--(17). That absence is **not** a historical novelty claim. The durable Mathia content is the exact combination of the already-established canonical off-critical zero with the joint holomorphy of the source-specific Mordell–Tornheim packet, which closes a specific loophole left open by PC-319.

## 6. Research consequence

PC-319 rules out coordinatewise zero confinement near weak coupling. PC-320 strengthens the boundary in the direction explicitly left live by the local mind synthesis: the obstruction is already a **full multivariable divisor** in an open neighborhood of the decoupled face. There is no isolated bad slice to discard, and no ordinary nonvanishing completion factor can remove it.

Accordingly, the surviving PC-316 program must do more than retain several Mellin variables or invoke a classical multivariable functional equation. It needs an independently justified destination theorem that selects a special locus, quotient, determinant, or coupled invariant not equal to the raw zero divisor of `Z`. A distinguished positive-coupling locus bounded away from `u=0` remains logically open, as does a different source-forced nonlinear coupling. So does a mixed-variable theorem whose relevant divisor is constructed from more than a single completed copy of (1).

What is now closed is the weaker escape

\[
\text{canonical PC-316 Mordell--Tornheim packet}
\longrightarrow
\text{full zero divisor / ordinary completion / coordinate mixing}
\longrightarrow
\text{Riemann-like zero confinement near }u=0.
\]

The local divisor already projects openly onto `(t,u)` while staying wholly in `Re(s)>1`.

## 7. Audit and falsification tests

The claim has five local checks:

1. verify the PC-319 inputs `A_5(s_0)=0`, `Re(s_0)>1`, and `B_7(T)\neq0`;
2. use (8)--(9) to verify normal convergence of (1) in a genuine complex polydisk crossing `u=0`;
3. compute the order `m` in the distinguished `s` variable at `(s_0,T,0)` from the exact factorization (5);
4. apply Weierstrass preparation to obtain (14) and check that the degree remains `m` on nearby `(t,u)` slices;
5. verify directly that a nonvanishing holomorphic factor preserves the zero set and that a biholomorphism preserves its local complex dimension.

Failure of the normal-convergence neighborhood or of the nonzero derivative in (12) would invalidate the hypersurface conclusion. Otherwise the result is local theorem-level complex analysis and requires neither a numerical zero computation nor any meromorphic continuation of the Mordell–Tornheim family.
