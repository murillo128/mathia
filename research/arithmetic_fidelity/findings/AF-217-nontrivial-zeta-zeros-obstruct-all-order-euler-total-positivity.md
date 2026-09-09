# AF-217 — nontrivial zeta zeros obstruct all-order Euler total positivity

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `FULL-EULER-GATE`, `EXACT-FIDELITY`, `CLASSICAL-BRIDGE`, `NO-NOVELTY-CLAIM`

## Claim

AF-216 gives an exact source-complexity gate for the first Dirichlet harmonic: bounded ordered sign variation limits how many consecutive real Dirichlet samples a finite signed source can annihilate. Its explicit boundary was that the full logarithmic Euler factor

\[
-\log(1-q^{-s})
=\sum_{\ell\ge 1}\frac{q^{-\ell s}}{\ell}
\tag{1}
\]

contains all higher harmonics, so the first-harmonic Chebyshev argument does not automatically transfer.

That boundary is genuine at all orders.

Put

\[
L(x):=-\log(1-e^{-x}),\qquad x>0,
\tag{2}
\]

and introduce logarithmic coordinates

\[
s=e^u,\qquad \lambda=e^{-v}.
\tag{3}
\]

Then the full one-generator Euler-log kernel is the translation kernel

\[
K(u,v):=L(e^{u-v}).
\tag{4}
\]

The kernel `K` is **not totally nonnegative of all orders**. Equivalently, after reversing the source coordinate back to increasing generator norm, the matrix family

\[
\Big[-\log(1-q_j^{-s_i})\Big]_{i,j}
\tag{5}
\]

is not sign-regular of all orders.

This obstruction persists even if the source nodes are required to be **rational primes**: there exist a finite order `n`, increasing positive real samples

\[
0<s_1<\cdots<s_n,
\tag{6}
\]

and increasing rational primes

\[
p_1<\cdots<p_n
\tag{7}
\]

such that

\[
\boxed{
(-1)^{n(n-1)/2}
\det\Big[-\log(1-p_j^{-s_i})\Big]_{i,j=1}^n<0.
}
\tag{8}
\]

The checkerboard factor in `(8)` is exactly the sign produced by reversing the source coordinate of a totally nonnegative translation kernel.

Consequently, ordered sign complexity by itself cannot yield an **all-order full-Euler analogue** of AF-216 through the classical total-positivity / variation-diminishing mechanism, even on genuine prime support. Some finite order must fail. A viable full-Euler recovery theorem must therefore stop at a proved finite order, retain extra structure, restrict the source category more strongly, or preserve a discriminator before the higher Euler harmonics are aggregated.

## Derivation

### 1. Exponential tilting reduces the kernel to a Pólya-frequency test

For any fixed `alpha>0`, define

\[
\Lambda_\alpha(t)
:=e^{\alpha t}L(e^t).
\tag{9}
\]

As `t\to-\infty`,

\[
L(e^t)=-\log(1-e^{-e^t})=-t+O(e^t),
\tag{10}
\]

so `e^{\alpha t}L(e^t)` is integrable at `-\infty`. As `t\to+\infty`,

\[
L(e^t)=e^{-e^t}+O(e^{-2e^t}),
\tag{11}
\]

so the decay is super-exponential. Hence

\[
\Lambda_\alpha\in L^1(\mathbb R),
\qquad \Lambda_\alpha>0.
\tag{12}
\]

Moreover

\[
\Lambda_\alpha(u-v)
=e^{\alpha u}e^{-\alpha v}K(u,v).
\tag{13}
\]

Every finite minor of the tilted kernel therefore differs from the corresponding minor of `K` only by a positive product of row and column factors. Thus

\[
\boxed{
K\text{ is totally nonnegative of all orders}
\iff
\Lambda_\alpha\text{ is a Pólya frequency function.}
}
\tag{14}
\]

The choice of `alpha>0` is only an integrability device; it does not change any determinant sign.

### 2. The bilateral Laplace transform is `Gamma zeta`

For `Re(z)<alpha`, substitute `x=e^t` into the bilateral Laplace transform:

\[
\begin{aligned}
\mathcal B\Lambda_\alpha(z)
&:=\int_{-\infty}^{\infty}
\Lambda_\alpha(t)e^{-zt}\,dt\\
&=\int_0^\infty
x^{\alpha-z-1}\big[-\log(1-e^{-x})\big]\,dx.
\end{aligned}
\tag{15}
\]

For `w=alpha-z` with `Re(w)>0`, the absolutely convergent expansion

\[
-\log(1-e^{-x})
=\sum_{m\ge1}\frac{e^{-mx}}m
\tag{16}
\]

gives

\[
\begin{aligned}
\mathcal B\Lambda_\alpha(z)
&=\sum_{m\ge1}\frac1m
\int_0^\infty x^{w-1}e^{-mx}\,dx\\
&=\Gamma(w)\sum_{m\ge1}m^{-(w+1)}\\
&=\boxed{\Gamma(\alpha-z)\zeta(\alpha-z+1)}.
\end{aligned}
\tag{17}
\]

This identity is exact on the transform half-plane and supplies a meromorphic continuation to the whole `z`-plane.

### 3. Schoenberg's theorem forbids the nontrivial zeta zeros

Schoenberg's characterization says that if an integrable function is Pólya frequency, then its bilateral Laplace transform has the form

\[
\mathcal B\Lambda(z)=\frac1{\Psi(z)}
\tag{18}
\]

on its strip of convergence, where `Psi` is an entire Laguerre--Pólya function. In particular, the meromorphic continuation of such a transform is the reciprocal of an entire function and therefore has **no zeros**.

Assume for contradiction that `K` were totally nonnegative of all orders. By `(14)`, `Lambda_alpha` would be Pólya frequency, so `(18)` would hold for some entire `Psi`. Combining `(17)` and `(18)` on the nonempty half-plane `Re(z)<alpha` and using uniqueness of meromorphic continuation would give

\[
\Gamma(\alpha-z)\zeta(\alpha-z+1)
=\frac1{\Psi(z)}.
\tag{19}
\]

Now choose any nontrivial zero `rho` of the Riemann zeta function and set

\[
z_\rho:=\alpha+1-\rho.
\tag{20}
\]

Then

\[
\alpha-z_\rho=\rho-1,
\tag{21}
\]

and `Gamma(rho-1)` is finite and nonzero because a nontrivial zeta zero is not an integer. Therefore the meromorphic continuation in `(17)` satisfies

\[
\Gamma(\rho-1)\zeta(\rho)=0.
\tag{22}
\]

But `1/Psi(z)` cannot vanish at a finite point. This contradicts `(19)`. Hence

\[
\boxed{K(u,v)=L(e^{u-v})\text{ is not totally nonnegative of all orders}.}
\tag{23}
\]

Only the established existence of nontrivial zeta zeros is used; RH is neither assumed nor obtained.

There is also a useful cancellation check on the analytic continuation. The trivial zeros of `zeta(w+1)` occur at negative odd integers `w=-3,-5,\ldots`, exactly where `Gamma(w)` has simple poles, so those zeros are canceled in the product. The obstruction in `(22)` is genuinely supplied by the nontrivial zero set.

### 4. Failure on the continuum can be transported to rational-prime nodes

Equation `(23)` means that for some finite `n` there are increasing real coordinates

\[
u_1<\cdots<u_n,
\qquad
v_1<\cdots<v_n
\tag{24}
\]

for which

\[
\det[K(u_i,v_j)]_{i,j=1}^n<0.
\tag{25}
\]

The inequality is strict, so by continuity it survives sufficiently small perturbations of the `v_j`.

For each rational prime `p`, define its source coordinate

\[
v_p:=-\log\log p.
\tag{26}
\]

These coordinates decrease to `-\infty`. They also have vanishing mesh in the tail. Indeed, if `p<q` are consecutive primes, Bertrand's postulate gives `q<2p`, hence

\[
0<v_p-v_q
=\log\frac{\log q}{\log p}
<\log\left(1+\frac{\log2}{\log p}\right)
\longrightarrow0.
\tag{27}
\]

Because `K` is translation invariant in the pair `(u,v)`, replacing every `u_i,v_j` in `(24)` by `u_i+C,v_j+C` leaves `(25)` unchanged. Choose `C<0` so far into the negative tail that the mesh in `(27)` is smaller than the perturbation tolerance from `(25)`. Then choose distinct primes `r_1>\cdots>r_n` so that

\[
v_{r_1}<\cdots<v_{r_n}
\tag{28}
\]

approximates `v_1+C,\ldots,v_n+C` closely enough to retain a negative determinant.

Set

\[
s_i:=e^{u_i+C}>0.
\tag{29}
\]

Since `e^{-v_r}=\log r`, the resulting matrix is

\[
K(u_i+C,v_{r_j})
=L(s_i\log r_j)
=-\log(1-r_j^{-s_i}).
\tag{30}
\]

Finally reorder the primes increasingly by `p_j=r_{n+1-j}`. Reversing `n` columns contributes the parity factor `(-1)^{n(n-1)/2}`, and `(25)` becomes exactly `(8)`.

Thus the all-order sign-regularity failure is not an artifact of arbitrary positive generator norms: **some finite prime-supported Euler-factor matrix already violates it**.

## Relation to AF-215 and AF-216

AF-215 shows that atomwise rational primality does not bound exact Prouhet cancellation order. AF-216 then identifies a genuinely relational repair for polynomial moments and the first Dirichlet harmonic: if the signed discrepancy has at most `r` ordered sign changes, the first `r+1` polynomial moments or equally spaced real Dirichlet samples cannot all vanish.

AF-217 closes the most tempting wholesale extension of that repair. The complete Euler logarithm is not an all-order variation-diminishing kernel. Higher prime-power harmonics collectively destroy total positivity at some finite order, and the obstruction is encoded analytically by the nontrivial zero set of `zeta` through `(17)`.

The resulting boundary is therefore sharper than "higher harmonics complicate the proof":

\[
\boxed{
\text{first harmonic: all-order Chebyshev/sign-variation gate}
\quad\not\Rightarrow\quad
\text{full Euler log: all-order sign-regular gate}.
}
\tag{31}
\]

This does not make sign complexity irrelevant. It says that sign complexity alone cannot be propagated through the full Euler aggregation by the strongest classical total-positivity mechanism at every order.

## Exact controls and boundaries

### The theorem is an all-order obstruction, not a low-order classification

Failure of total nonnegativity means that **some finite order** has a bad minor. The argument does not identify the smallest failing order, nor does it rule out total positivity or sign regularity through a substantial finite range.

Therefore a finite-order Euler theorem tailored to a bounded source complexity remains possible and should be tested separately.

### No explicit bad prime minor is supplied

The prime-support step is existence-by-density in logarithmic source coordinates. It proves that a finite rational-prime witness exists, but it does not locate the smallest primes, the smallest matrix size, or a numerically well-conditioned witness.

A bounded computation could search for such a witness, but an explicit example is not needed for the exact no-go `(8)`.

### The result does not show instability on every bounded-sign class

Non-total-positivity rules out a universal all-order variation-diminishing law. It does not prove that every source with `r` sign changes is poorly conditioned, nor that every finite sampling design fails. Quantitative conditioning, source localization, coefficient size, and bandwidth remain independent gates.

### The prime approximation uses only source support, not canonical prime weights

Equation `(8)` uses a finite set of genuine rational primes but does not assert that the canonical von Mangoldt measure, the full prime sequence with its natural weights, or a particular RH-facing discrepancy realizes the bad coefficient pattern.

A stronger non-hereditary prime source law may still exclude the finite witness. As in AF-215 and AF-216, that law must be derived from the concrete arithmetic mechanism rather than added because it restores a desired theorem.

### This is not a proof or reformulation of RH

The contradiction uses only the known existence of nontrivial zeta zeros. Their real parts play no role. The result therefore gives an unconditional compression obstruction and no information about whether those zeros lie on the critical line.

## Prior art and novelty assessment

The central analytic ingredients are classical and no novelty is claimed for them.

- I. J. Schoenberg, **"On Pólya frequency functions. I. The totally positive functions and their Laplace transforms,"** *Journal d'Analyse Mathématique* **1** (1951), 331--374, DOI `10.1007/BF02790092`. This is the primary source for the Laplace-transform characterization of Pólya frequency functions used in `(18)`.
- I. J. Schoenberg, **"On Pólya frequency functions. II. Variation-diminishing integral operators of the convolution type,"** *Acta Scientiarum Mathematicarum (Szeged)* **12** (1950), 97--106. This is the classical variation-diminishing counterpart of total positivity.
- Karlheinz Gröchenig, **"Schoenberg's Theory of Totally Positive Functions and the Riemann Zeta Function,"** arXiv:`2007.12889` (2020). The paper gives a modern statement of Schoenberg's characterization and develops a separate connection between Pólya-frequency functions, the Laguerre--Pólya class, and the Riemann xi-function/RH. It is direct prior art that total positivity and the zeta zero problem are already linked in the literature.
- NIST Digital Library of Mathematical Functions, §25.10, records that `zeta` has infinitely many nontrivial zeros in `0<Re(s)<1`; only their existence is required here.

The Mellin identity `(17)` is derived directly from the elementary Euler-log expansion `(16)`. Bertrand's postulate supplies the prime-coordinate mesh argument in `(27)`.

A targeted search did not supply a source needed for the exact `L(e^t)` Euler-log specialization or the prime-node transport `(26)`--`(30)`, but absence of a located reference is not evidence of novelty. The durable Arithmetic Fidelity result should be treated conservatively as a **literature-derived compression obstruction**: Schoenberg's classical transform theorem, applied to the exact Euler-log profile, shows that AF-216's all-order sign-complexity repair cannot survive full Euler aggregation unchanged.

## Consequence for the Arithmetic Fidelity frontier

The source-side frontier now has two distinct gates.

First, AF-216 proves that bounded ordered sign complexity genuinely blocks arbitrary exact cancellation before full Euler aggregation. Second, AF-217 proves that the complete Euler logarithm does not preserve the all-order total-positivity structure needed to carry that bound through automatically, even when the support consists of actual rational primes.

The next useful question is therefore **finite-order and source-specific**: for a declared sign budget or arithmetic complexity class, determine the largest Euler order/band on which sign regularity or a quantitative lower modulus still holds, and identify which additional prime-derived relation prevents the finite bad minors guaranteed by AF-217 from becoming admissible controls. A successful theorem must state both sides of the transport: the source restriction that limits cancellation and the observation structure that preserves that restriction far enough downstream to matter.