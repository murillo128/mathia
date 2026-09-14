# AF-336 — Half-spectrum vanishing rigidifies the unit-circle fiber to one regular-polygon orbit

**Status:** `EXACT-DERIVED`, `CLASSICAL-IDENTITY+DERIVED`, `ARITHMETIC-FIDELITY`, `STRUCTURAL-RECOVERY`, `DIMENSION-TIGHT`, `ARITHMETIC-CONTROL`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

Let

\[
Z=\{z_1,\ldots,z_n\}\subset S^1,
\qquad n\ge3,
\]

be an unordered multiset, allowing multiplicity, and write

\[
s_k(Z)=\sum_{j=1}^n z_j^k,
\qquad
q=\left\lfloor\frac n2\right\rfloor.
\]

Then the first half of the positive Fourier/power-sum spectrum already has a globally rigid zero fiber:

\[
\boxed{
s_1(Z)=s_2(Z)=\cdots=s_q(Z)=0
\iff
Z=\rho\,\mu_n
\text{ for some }\rho\in S^1.
}
\tag{1}
\]

Thus the entire zero fiber consists exactly of the common-rotation orbit of the regular `n`-gon. Equivalently, on the centered source `s_1=0`, the low-harmonic compression

\[
H_q(Z)=(s_2(Z),\ldots,s_q(Z))
\tag{2}
\]

has

\[
\boxed{H_q^{-1}(0)=\{\rho\mu_n:\rho\in S^1\}.}
\tag{3}
\]

The threshold is locally sharp. At a regular `n`-gon, if only the first `r<q` harmonics are required to vanish, the ordered zero fiber is locally a smooth real manifold of dimension

\[
\boxed{n-2r,}
\tag{4}
\]

so after quotienting common rotation it still has local dimension

\[
\boxed{n-2r-1>0.}
\tag{5}
\]

At the half-spectrum threshold `q`, the local zero fiber drops to the single rotation direction. For odd `n=2m+1`, the `m` complex harmonic equations have real rank `n-1`; for even `n=2m`, the first `m-1` harmonics contribute `2m-2` real ranks and the self-paired middle harmonic contributes exactly one more, again giving total rank `n-1`.

The product phase

\[
E(Z)=\prod_{j=1}^n z_j
\tag{6}
\]

is a global coordinate on the collision fiber `(3)`: each `E\in S^1` determines exactly one unordered rotated regular `n`-gon. Hence at the maximally singular harmonic value `H_q=0`, the missing information is not merely one-dimensional in a local count; it is **globally exactly one circle-valued provenance variable**.

For distinct rational primes `p_1,\ldots,p_n`, define

\[
F_P(t)=\sum_{j=1}^n p_j^{-it}.
\tag{7}
\]

Then the regular-polygon collision fiber is arithmetically inaccessible at nonzero real time. In particular,

\[
\boxed{
F_P(t)=F_P(2t)=\cdots=F_P(qt)=0
\quad\text{has no real solution }t.
}
\tag{8}
\]

This does **not** settle the weaker eight-prime singular incidence from AF-328--AF-335, where centering and `e_4=0` do not force all low harmonics to vanish. It instead gives the exact global endpoint of the consecutive-harmonic compression: once half of the positive spectrum vanishes, no hidden nonregular unitary configuration remains, and rational-prime phases cannot enter the unique residual orbit.

No RH consequence is claimed.

## 1. Newton identities turn half-spectrum vanishing into half-coefficient vanishing

Let

\[
P_Z(w)=\prod_{j=1}^n(w-z_j)
=\sum_{k=0}^n(-1)^k e_k w^{n-k},
\qquad
E=e_n.
\tag{9}
\]

Newton's identities give recursively

\[
k e_k
=\sum_{j=1}^k(-1)^{j-1}e_{k-j}s_j,
\qquad e_0=1.
\tag{10}
\]

Therefore

\[
s_1=\cdots=s_q=0
\quad\Longrightarrow\quad
\boxed{e_1=\cdots=e_q=0.}
\tag{11}
\]

Because every root lies on `S^1`, the coefficient system is self-inversive:

\[
\boxed{e_{n-k}=E\,\overline{e_k}.}
\tag{12}
\]

For odd `n=2m+1`, equation `(11)` kills `e_1,\ldots,e_m`, while `(12)` kills `e_{m+1},\ldots,e_{2m}`. For even `n=2m`, `(11)` kills `e_1,\ldots,e_m`, and `(12)` kills `e_{m+1},\ldots,e_{2m-1}`. Thus in either parity

\[
\boxed{e_1=e_2=\cdots=e_{n-1}=0.}
\tag{13}
\]

The root polynomial reduces to

\[
P_Z(w)=w^n+(-1)^nE.
\tag{14}
\]

Since `|E|=1`, its roots are precisely a rotated copy of all `n`-th roots of unity. This proves the forward implication in `(1)`. The reverse implication is the standard roots-of-unity identity

\[
\sum_{z\in\rho\mu_n}z^k=0,
\qquad 1\le k\le n-1.
\tag{15}
\]

So `(1)` is global and includes multiplicities automatically: polynomial `(14)` has `n` distinct roots.

## 2. The half-spectrum threshold is locally minimal

Fix a rotated regular polygon

\[
z_j=\rho\omega^j,
\qquad
\omega=e^{2\pi i/n},
\qquad
j=0,\ldots,n-1.
\tag{16}
\]

Write an infinitesimal unit-circle deformation as

\[
z_j(\varepsilon)=z_j e^{i\varepsilon u_j},
\qquad u_j\in\mathbb R.
\tag{17}
\]

Then

\[
D s_k(u)
=ik\rho^k\sum_{j=0}^{n-1}\omega^{jk}u_j.
\tag{18}
\]

For `1\le k<n/2`, the real and imaginary parts of the `k`-th discrete Fourier mode give two independent real linear functionals. Different `k` give orthogonal Fourier modes. Hence for every `r<n/2`,

\[
\operatorname{rank}_{\mathbb R}D(s_1,\ldots,s_r)=2r.
\tag{19}
\]

The implicit-function theorem therefore gives a local zero manifold of dimension `n-2r`, proving `(4)`. Common rotation is the constant Fourier mode and lies in this kernel, so quotienting it leaves `(5)`.

At the threshold there are two parity cases.

For odd `n=2m+1`, all `m=q` frequencies satisfy `k<n/2`, so

\[
\operatorname{rank}_{\mathbb R}D(s_1,\ldots,s_m)=2m=n-1.
\tag{20}
\]

For even `n=2m`, frequencies `1,\ldots,m-1` contribute `2m-2` real ranks. The middle mode is

\[
D s_m(u)
=im\rho^m\sum_{j=0}^{n-1}(-1)^j u_j,
\tag{21}
\]

which runs along one fixed real line in `\mathbb C` and contributes one additional independent real rank. Thus

\[
\operatorname{rank}_{\mathbb R}D(s_1,\ldots,s_m)=2m-1=n-1.
\tag{22}
\]

The threshold zero fiber is therefore locally one-dimensional in either parity, exactly matching the common-rotation orbit already identified globally in `(1)`.

This gives a sharp compression statement: fewer than `floor(n/2)` consecutive positive harmonics leave genuine shape freedom near the regular polygon; the half-spectrum value removes all shape freedom and leaves only global phase.

## 3. Product phase is the exact global coordinate on the residual fiber

On the fiber `(3)`, equation `(14)` shows that the unordered root set is determined by `E` alone:

\[
Z(E)=\{w\in S^1:w^n=(-1)^{n+1}E\}.
\tag{23}
\]

Conversely every `E\in S^1` defines exactly one such unordered regular polygon. Therefore

\[
\boxed{
H_q^{-1}(0)\ \cong\ S^1
\quad\text{via}\quad E.
}
\tag{24}
\]

This sharpens the dimension statement in AF-335 at the most singular output. AF-335 proves that the product phase repairs a one-real-dimensional local fidelity defect on a nonempty open middle-singular patch. Here the zero harmonic fiber can be classified globally: there are no additional branches, nonregular shapes, or hidden finite aliases. The scalarized half-spectrum has forgotten exactly the circle coordinate `E`.

In design language, `(1)` says that an equal-weight `n`-point configuration on `S^1` whose Fourier moments vanish through degree `floor(n/2)` must be the regular `n`-gon. The local rank calculation also explains why the cutoff is tight for consecutive harmonics rather than merely sufficient by Newton reconstruction.

## 4. Rational-prime phases cannot enter the regular-polygon fiber

Let `p_1,\ldots,p_n` be distinct rational primes with `n\ge3`, and suppose for contradiction that some real `t` satisfies `(8)`. Since `F_P(0)=n`, necessarily `t\ne0`.

Set

\[
z_j=p_j^{-it}.
\tag{25}
\]

By `(1)`, the phase multiset is a rotated regular `n`-gon. Hence for any `a,b`,

\[
(z_a/z_b)^n=1.
\tag{26}
\]

Choose three distinct primes `p_1,p_2,p_3`. There are integers `A,B` such that

\[
nt\log(p_1/p_2)=2\pi A,
\qquad
nt\log(p_1/p_3)=2\pi B.
\tag{27}
\]

Neither `A` nor `B` is zero: if, for example, `A=0`, then `p_1=p_2` because `t\ne0`. Thus

\[
\frac{\log(p_1/p_2)}{\log(p_1/p_3)}=\frac AB\in\mathbb Q.
\tag{28}
\]

Clearing the rational ratio gives a nontrivial multiplicative relation among the three distinct primes. Explicitly,

\[
(p_1/p_2)^B=(p_1/p_3)^A,
\tag{29}
\]

contradicting unique factorization. Therefore `(8)` is impossible.

This is the same elementary torsion obstruction used in the five-point special case AF-313, but `(1)` shows that it applies uniformly at the exact half-spectrum threshold for every support size.

## 5. Fidelity consequence and boundary with the current eight-prime frontier

The result identifies an exact endpoint for one natural compression family. For consecutive harmonic truncation on equal-weight unit-circle configurations,

\[
(s_1,\ldots,s_r),
\tag{30}
\]

there is genuine local shape ambiguity at the regular polygon for every `r<floor(n/2)`. At `r=floor(n/2)`, that ambiguity collapses globally to one known gauge orbit, and the product phase is a complete coordinate on it.

That is stronger than a dimension heuristic: it gives the entire collision class and an exact minimal retained mark at the singular output. It is also a useful falsification control for arithmetic specializations. A proposed prime mechanism that requires simultaneous vanishing of the full consecutive half-spectrum is dead unconditionally; the rational-prime common-time orbit cannot realize the only unitary geometry compatible with those vanishing moments.

The surviving AF-328--AF-335 problem is weaker and therefore genuinely different. For eight phases, centering `e_1=0` together with middle singularity `e_4=0` imposes only two coefficient conditions. Newton's identities do not turn that pair into

\[
s_1=s_2=s_3=s_4=0.
\]

So the present no-go theorem cannot be used to claim that the eight-prime singular target is empty. Instead it marks a nearby boundary: adding enough low-harmonic vanishing to reach the half-spectrum immediately rigidifies the target to torsion and lets prime multiplicative independence kill it.

## Prior art and novelty assessment

All ingredients are classical, and no broad novelty is claimed.

- Philippe Delsarte, Jean-Marie Goethals, and Johan Jacob Seidel, **“Spherical codes and designs,”** *Geometriae Dedicata* 6 (1977), 363--388, DOI `10.1007/BF03187604`, is foundational prior art for finite spherical designs. On `S^1`, vanishing of the positive Fourier modes through degree `q` is the equal-weight trigonometric/spherical-design condition through that degree.
- Christopher D. Sinclair and Jeffrey D. Vaaler, **“Self-inversive polynomials with all zeros on the unit circle,”** in *Number Theory and Polynomials*, London Mathematical Society Lecture Note Series 352, Cambridge University Press (2010), 312--321, DOI `10.1017/CBO9780511721274.020`, is direct prior art for the coefficient symmetry `(12)`.
- Newton identities and finite power-sum reconstruction are classical symmetric-function mathematics. I. G. Macdonald, *Symmetric Functions and Hall Polynomials*, 2nd ed., Oxford University Press (1995), is standard background.

A targeted search found the standard spherical-design, self-inversive-polynomial, and moment-reconstruction frameworks, but no reason to present `(1)` as a new general theorem. It is an elementary synthesis of those structures. The durable Arithmetic Fidelity content is the exact compression classification: **half-spectrum zero data leaves precisely one global phase orbit, fewer consecutive harmonics leave positive-dimensional shape ambiguity, and distinct rational-prime phases cannot occupy that final collision fiber.**

## Boundaries and falsification checks

- The result concerns **equal-weight unit-circle** configurations. Unequal weights, off-circle nodes, approximate moment cancellation, or noisy observations are different problems.
- The threshold is sharp for the consecutive harmonic family `s_1,\ldots,s_r`; it does not claim optimality among arbitrary nonlinear observables or arbitrary sparse frequency sets.
- The local dimension statement is made on the ordered configuration torus. Passing to unordered configurations is a finite quotient near a regular polygon and does not change the local dimension; quotienting common rotation removes one real dimension.
- The prime no-go theorem requires at least three distinct primes. This line studies `n\ge3`, so that condition is automatic in the stated specialization.
- Equation `(8)` rules out simultaneous vanishing through `q`; it does not rule out a single zero of `F_P(t)`, a sparse set of harmonic zeros, or the weaker coefficient incidence `e_1=e_{n/2}=0` for even support.
- Exact rigidity says nothing by itself about conditioning near the zero fiber. AF-319--AF-327 treat finite-height conditioning and approximate phase filling separately.
- No zero-selection theorem, critical-line statement, or RH implication follows.

## Dependency audit

- **AF-313:** proves the five-point special phenomenon and excludes its regular-pentagon collision for rational-prime phases.
- **AF-316:** supplies the general parity-controlled self-inversive recovery mechanism; the present finding extracts and sharpens the exact zero-fiber geometry for every support size.
- **AF-335:** shows that even middle singularity carries a one-real-dimensional local fidelity defect and that the product phase is a minimal continuous lift on an open singular patch. The present finding identifies the complete global collision fiber at the maximally singular harmonic output and shows that the same phase mark is an exact global coordinate there.
- **This finding:** closes the consecutive-half-spectrum branch. Further progress on the current eight-prime singular gate must use weaker/joint coefficient constraints, source-specific incidence information, or nonconsecutive relational data rather than requiring all low harmonics to vanish.