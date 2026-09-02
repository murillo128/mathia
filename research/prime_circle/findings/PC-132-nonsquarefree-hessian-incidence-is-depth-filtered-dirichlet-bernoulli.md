# PC-132 — nonsquarefree Hessian incidence is depth-filtered Dirichlet–Bernoulli data

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-STRUCTURE` + `PRIOR-ART-REDIRECTION` + `DECISIVE-NEGATIVE` for treating repeated-prime-power depth in the linear multiplicative-character coordinates of a PC-128 cross-shell inverse-square Hessian as a new arithmetic or RH-sensitive coefficient alphabet. This does not diagonalize the finite Hessian, classify nonlinear eigenvalue/singular-value invariants, or address coherent cross-level/infinite operators or PC-017's global uniformization/monodromy branch.

PC-131 classified every linear character coefficient for distinct **squarefree** noncoprime shells and left repeated prime powers as the first finite local-depth escape. That escape also closes. For arbitrary distinct shell indices `m,n`, the additive Fourier transform of an endpoint character factors prime by prime. At a prime power, a nonprincipal local character has one exact Fourier valuation shell determined by the difference between modulus exponent and conductor exponent, while a principal local character contributes only the two adjacent Ramanujan valuation shells. Consequently, two endpoint characters can couple only when their local lift depths are compatible. Every surviving global coefficient then reduces to one fixed generalized-Bernoulli value `L(-1,eta)` times explicit Gauss/local factors, or to a finite divisor polynomial in the principal product channel.

Repeated prime powers therefore add **valuation selection rules**, not a new analytic family. The squarefree formulas of PC-131 are the depth-zero specialization of the same finite Fourier mechanism.

## 1. The arbitrary-modulus cross-shell coefficient

Let `m,n>1` be distinct, with no squarefreeness assumption, and put

\[
L=\operatorname{lcm}(m,n),\qquad M=L/m,\qquad N=L/n.
\]

For endpoint units `a in U(m)` and `b in U(n)`, the PC-128 conductance block is

\[
C_{m,n}(a,b)
=\frac1{4\sin^2\!\bigl(\pi(Ma-Nb)/L\bigr)}.
\]

For multiplicative characters `chi mod m` and `psi mod n`, with normalized endpoint bases as in PC-130/131, write

\[
\mathcal M_{\chi,\psi}
:=\langle e_\chi,C_{m,n}f_\psi\rangle.
\]

Let

\[
G_\rho^{(q)}(k)
:=\sum_{u\in U(q)}\rho(u)e^{2\pi i k u/q}.
\]

The universal cyclic inverse-square transform used in PC-131 is valid for every `L`, so exactly as there,

\[
\boxed{
\mathcal M_{\chi,\psi}
=-\frac1{L\sqrt{\varphi(m)\varphi(n)}}
\sum_{k=0}^{L-1}
\lambda_k
G_{\overline\chi}^{(m)}(k)
G_\psi^{(n)}(-k),
}
\]

with

\[
\lambda_k=\frac{k(L-k)}2.
\]

The constant Fourier mode again vanishes because `Ma=Nb mod L` would identify roots of the two distinct exact orders. Thus the only new issue beyond PC-131 is the full imprimitive prime-power structure of the two generalized Gauss transforms.

## 2. Exact local Fourier transform at a prime power

Fix a prime power `p^a` and a local Dirichlet character `theta mod p^a`. Let its conductor be `p^b`.

If `b>0`, let `theta*` denote the primitive character modulo `p^b` inducing `theta`. Splitting a unit modulo `p^a` into its residue modulo `p^b` and its `p^{a-b}` lifts gives the exact identity

\[
\boxed{
G_{\theta}^{(p^a)}(k)
=
\begin{cases}
 p^{a-b}\tau(\theta^*)\,
 \overline{\theta^*\!\left(k/p^{a-b}\right)},
 &p^{a-b}\mid k,\\[3pt]
 0,&p^{a-b}\nmid k.
\end{cases}
}
\]

Here the primitive character is extended by zero off the units. Hence the first line is itself zero when `p` divides `k/p^{a-b}`. Equivalently,

\[
\boxed{
G_{\theta}^{(p^a)}(k)\ne0
\Longrightarrow
v_p(k)=a-b.
}
\]

The integer

\[
\boxed{\delta_p(\theta):=a-b}
\]

is therefore the exact **Fourier lift depth** of a nonprincipal local character.

If `b=0`, the local character is principal and the transform is the prime-power Ramanujan sum

\[
\boxed{
G_{1}^{(p^a)}(k)
=c_{p^a}(k)
=p^a\mathbf1_{p^a\mid k}
-p^{a-1}\mathbf1_{p^{a-1}\mid k}.
}
\]

Thus a principal local factor has no hidden higher-depth transform: it is a linear combination of only two adjacent divisibility indicators.

For a general modulus `q=prod_p p^{a_p}`, CRT factors `G_theta^(q)` into these local transforms, with only unit phases coming from the CRT idempotents. Those phases do not change the valuation support. This prime-power statement is the exact replacement for the squarefree Gauss × Ramanujan factorization used in PC-131.

## 3. Repeated prime powers impose a local depth-matching selection rule

Write

\[
a_p=v_p(m),\qquad c_p=v_p(n),
\]

and let

\[
b_p=v_p(\operatorname{cond}\chi),
\qquad
d_p=v_p(\operatorname{cond}\psi).
\]

When `b_p>0`, the local factor from `G_{overline chi}^{(m)}(k)` can be nonzero only at

\[
v_p(k)=a_p-b_p.
\]

When `d_p>0`, the local factor from `G_psi^(n)(-k)` can be nonzero only at

\[
v_p(k)=c_p-d_p.
\]

Therefore, if both endpoint characters are locally nonprincipal at `p`,

\[
\boxed{
a_p-b_p\ne c_p-d_p
\Longrightarrow
\mathcal M_{\chi,\psi}=0.}
\]

This is the new repeated-power feature: two characters with the same primitive-looking finite harmonic type can fail to interact solely because they sit at different imprimitive lift depths.

If exactly one endpoint is locally nonprincipal, say `b_p>0` and `d_p=0`, then `v_p(k)=a_p-b_p` is fixed and the principal factor on the other endpoint is just the scalar

\[
c_{p^{c_p}}\!\left(p^{a_p-b_p}\right).
\]

It vanishes when `a_p-b_p<c_p-1` and otherwise contributes only the elementary values `-p^{c_p-1}` or `phi(p^{c_p})`. The symmetric statement holds when only `psi` is locally nonprincipal. If both local characters are principal, the product is merely a finite combination of divisibility indicators obtained from the displayed Ramanujan formula.

So prime-power depth can create exact zeros and elementary local weights, but no new local special function.

## 4. Every surviving nonprincipal global channel contains one fixed `L(-1,eta)` value

Assume the local selection rules do not kill the coefficient. Let

\[
f=\operatorname{cond}\chi,
\qquad h=\operatorname{cond}\psi,
\qquad \ell=\operatorname{lcm}(f,h).
\]

Inflate the primitive local ancestors to modulus `ell` and define, exactly as in PC-131,

\[
\boxed{\eta=\chi^*\overline{\psi^*}}
\]

as a Dirichlet character modulo `ell`, with zero extension away from the units.

At every prime where at least one endpoint is locally nonprincipal, the preceding section fixes one exact valuation `delta_p` of `k`. Put

\[
D=\prod_{p\mid\ell}p^{\delta_p}.
\]

The compatibility conditions imply

\[
\boxed{\ell\mid L/D.}
\]

After writing `k=Dt`, all nonprincipal local factors combine, up to an explicit product `K_{chi,psi}` of powers of primes, Gauss sums, CRT unit phases, and the scalar principal factors from mixed channels, into

\[
K_{\chi,\psi}\,\eta(t).
\]

The primes at which **both** endpoint characters are principal lie outside `ell`. Their remaining Ramanujan product has a finite indicator expansion

\[
\boxed{
R(t)=\sum_{H\in\mathcal H}r_H\mathbf1_{H\mid t},
}
\]

where `r_H` are explicit integers, every `H` divides `L/D`, and `(H,ell)=1`. No approximation is involved; this follows by multiplying the two-term prime-power Ramanujan formulas.

Hence the Fourier numerator is a finite sum of terms

\[
\sum_{\substack{0\le t<L/D\\H\mid t}}
\lambda_{Dt}\eta(t).
\]

If `eta` is nonprincipal, put `t=Hu`. Since `(H,ell)=1` and `ell | L/(DH)`, the standard generalized-Bernoulli quadratic sum gives

\[
\boxed{
\sum_{\substack{0\le t<L/D\\H\mid t}}
\lambda_{Dt}\eta(t)
=DH\,L\,\eta(H)L(-1,\eta).
}
\]

Therefore every surviving nonprincipal product channel has the exact form

\[
\boxed{
\mathcal M_{\chi,\psi}
=-\frac{K_{\chi,\psi}D}
{\sqrt{\varphi(m)\varphi(n)}}
L(-1,\eta)
\sum_{H\in\mathcal H}r_HH\eta(H).
}
\]

All dependence on repeated prime powers is in the explicit lift-depth selection, Gauss factors, prime powers, and finite local polynomial. The **only analytic special value is the same fixed `L(-1,eta)` / generalized-Bernoulli datum already present in PC-131**. There is no free complex parameter.

Parity zeros remain automatic: if `eta(-1)=-1`, then `L(-1,eta)=0`.

## 5. Principal product channels remain finite divisor algebra

If `eta` is principal modulo `ell`, the generalized-Bernoulli reduction above is replaced by a finite coprimality count, not by a new analytic object. Insert

\[
\mathbf1_{(t,\ell)=1}
=\sum_{e\mid\ell}\mu(e)\mathbf1_{e\mid t}
\]

into each `H`-term. The only needed universal quadratic sum is the one already used in PC-131,

\[
\boxed{
T_A(L)
:=\sum_{\substack{0\le k<L\\A\mid k}}\lambda_k
=\frac{L(L^2-A^2)}{12A}.
}
\]

Consequently every principal product channel is an explicit finite combination of

\[
T_{D\operatorname{lcm}(H,e)}(L),
\qquad H\in\mathcal H,\ e\mid\ell,
\]

multiplied by the already-explicit local Gauss/CRT normalization. Thus cancellation of the endpoint characters does not reveal a new `L`-family; it leaves finite divisor/Bernoulli algebra.

Sections 2–5 classify the **linear multiplicative-character coefficient alphabet for arbitrary distinct `m,n`**, including all repeated prime powers.

## 6. Exact depth audit at `(m,n)=(4,8)`

The smallest repeated-power example already exhibits the new selection rule. Ordering `U(4)=(1,3)` and `U(8)=(1,3,5,7)`, the conductance block is

\[
C_{4,8}
=\frac12
\begin{pmatrix}
2+\sqrt2&2+\sqrt2&2-\sqrt2&2-\sqrt2\\
2-\sqrt2&2-\sqrt2&2+\sqrt2&2+\sqrt2
\end{pmatrix}.
\]

Let `chi_{-4}` be the nonprincipal character modulo `4`. Its local conductor exponent is `2`, equal to the modulus exponent, so its lift depth is `0`.

First take on `U(8)` the character induced from `chi_{-4}`. Its conductor is still `4`, so its lift depth at `2` is `3-2=1`. The depths mismatch and the theorem predicts

\[
\boxed{\mathcal M_{\chi_{-4},\,\chi_{-4}\uparrow 8}=0.}
\]

This is immediate from the displayed matrix: the induced column character is `(1,-1,1,-1)`, which cancels inside each equal column pair.

Now take the primitive character `chi_{-8}` on `U(8)`, whose values are `(1,1,-1,-1)`. Its lift depth is `0`, matching `chi_{-4}`. Direct exact multiplication gives

\[
\boxed{\mathcal M_{\chi_{-4},\chi_{-8}}=2.}
\]

The product character is the even primitive `chi_8`, and

\[
L(-1,\chi_8)=-1.
\]

Thus the first genuinely nonsquarefree test shows exactly what the general formula says: repeated depth first acts as a hard Fourier support filter; once the depths match, the surviving number returns immediately to the fixed generalized-Bernoulli package.

## 7. Prior-art and novelty audit

No theorem-level historical novelty is claimed for the finite Fourier ingredients.

- The local formulas in Section 2 are the standard finite Fourier transform of an induced Dirichlet character at a prime power; the principal case is the classical Ramanujan sum. Their CRT product is ordinary finite harmonic analysis.
- Beck–Halloran, already anchored in `research/prime_circle/SOURCES.md`, places trigonometric character sums inside the established discrete-Fourier/class-number framework.
- Gao–Guo, also already anchored there, treats trigonometric determinants for **arbitrary positive moduli** through Dirichlet special values, Gauss sums, and spectral decomposition. This is a particularly strong novelty warning for interpreting repeated prime powers in a finite trigonometric matrix as a new `L`-mechanism.
- The identity `L(1-r,eta)=-B_{r,eta}/r`, anchored through Szmidt–Urbanowicz–Zagier, supplies the generalized-Bernoulli interpretation of the quadratic character sums.

Directed searches around imprimitive Gauss transforms, prime-power trigonometric character sums, arbitrary-modulus trigonometric determinants, and cosecant-squared character matrices found these standard/local and Gao–Guo/Beck–Halloran neighborhoods, not evidence for a distinct RH mechanism generated by conductor lift depth. The exact two-modulus Prime-Circle bookkeeping above is a project-specific scope classification, not a priority claim.

PC-132 also avoids duplicating PC-125: the latter already classifies arbitrary shell-ratio **multisets** cyclotomically. The result here concerns the remaining endpoint incidence of the PC-128 rectangular Hessian after multiplicative Fourier transformation. It extends PC-131 from squarefree moduli to the full prime-power local theory.

## 8. Research consequence and boundary

The explicit finite boundary left by PC-131 is now closed:

\[
\boxed{
\text{arbitrary noncoprime PC-128 Hessian incidence}
\xrightarrow{\text{endpoint character transform}}
\text{valuation-depth filters}\times
\bigl(L(-1,\eta)\text{ / finite divisor data}\bigr).
}
\]

So **genuinely nonsquarefree local depth does not create a new linear harmonic alphabet**. It can delete character channels and change elementary local weights, but every surviving coefficient remains in the classical Gauss–Dirichlet–Bernoulli package. In particular, repeated prime powers do not supply a free complex spectral parameter, gamma factor, functional equation, or critical-line selector at this level.

The obstruction remains deliberately linear. It does not show that nonlinear spectral invariants of `C_{m,n}` or the full Laplacian `L_{m,n}` are elementary, nor that a coherent product of several levels is reducible to one fixed character table. It does not address an intrinsically forced infinite-level renormalization, noncommutative ordered memory, or PC-017's global primitive-only uniformization/monodromy defect.

The finite coefficient frontier is nevertheless complete for the PC-128 bipartite Hessian: coprime incidence is PC-130, squarefree noncoprime incidence is PC-131, and arbitrary repeated-power incidence is the depth-filtered extension above. Any surviving Hessian-based RH mechanism must now use **nonlinear organization or cross-level/infinite structure**, not claim new arithmetic from a single finite matrix's linear multiplicative-character coordinates.