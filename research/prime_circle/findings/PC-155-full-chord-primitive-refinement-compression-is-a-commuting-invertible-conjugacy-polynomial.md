# PC-155 — full-chord primitive refinement compression is a commuting invertible conjugacy polynomial

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-NEGATIVE` for the canonical **fiber-constant cross-level compression** of the full primitive-shell inverse-square chord operator. PC-039 explicitly left primitive-shell refinement outside its divisor-subpolygon Kron theorem; PC-148 proved exact CRT-flatness only for the dominant gap-two matching skeleton; and PC-154 still left cross-level coherent transport of the full all-chord operator open. The most direct such transport can now be classified exactly.

Let

\[
U(N):=(\mathbb Z/N\mathbb Z)^\times
\]

and let `L_N^{int}` be the full inverse-square chord Laplacian on the primitive shell,

\[
(L_N^{\rm int}f)(a)
=\sum_{\substack{b\in U(N)\\b\ne a}}
\frac{f(a)-f(b)}{4\sin^2(\pi(a-b)/N)}.
\tag{1}
\]

Use the normalization of PC-151--PC-154,

\[
A_N:=N^{-2}L_N^{\rm int}.
\tag{2}
\]

If `q` is prime and `q\nmid N`, reduction `U(Nq) -> U(N)` has exactly `q-1` points in every fiber. Let `J_{N,q}` be the normalized pullback of a coarse function to a fiber-constant fine function. Then the complete fine operator compresses exactly to

\[
\boxed{
J_{N,q}^*A_{Nq}J_{N,q}
=
\frac{q-2}{q-1}A_N
+
\frac{1}{q^2(q-1)}V_qA_NV_q^{-1},
}
\tag{3}
\]

where

\[
(V_qf)(a):=f(q^{-1}a)
\tag{4}
\]

is the multiplicative permutation of the coarse primitive shell. Thus adjoining a prime does not generate a new coarse operator algebra: it applies the explicit superoperator

\[
\boxed{
\mathcal S_q
=
\frac{q-2}{q-1}I
+
\frac{1}{q^2(q-1)}\operatorname{Ad}_{V_q}.
}
\tag{5}
\]

For squarefree refinements the prime-step superoperators commute exactly, every step is invertible, and after removing the classical two-point Mertens/Schemmel scalar, the residual character-channel product is absolutely convergent and nonzero. Consequently this canonical cross-level compression cannot manufacture an ordered-prime holonomy, a new zero divisor, or a critical-line mechanism from the full primitive-shell chord operator.

## 1. Exact prime-step compression from the cosecant distribution law

Let `R_{N,q}` be the unnormalized fiber incidence matrix,

\[
R_{N,q}(a,x)=1_{x\equiv a\pmod N},
\qquad
a\in U(N),\ x\in U(Nq).
\tag{6}
\]

Since every coarse unit has `q-1` unit lifts,

\[
R_{N,q}R_{N,q}^*=(q-1)I,
\qquad
J_{N,q}:=\frac1{\sqrt{q-1}}R_{N,q}^*.
\tag{7}
\]

Fix distinct `a,b in U(N)` and put `h=a-b mod N`. By CRT, identify the two fibers with nonzero residues `u,v in F_q^*`. For their fiber difference

\[
t=u-v\in\mathbb F_q
\]

the number of ordered pairs is

\[
M_0=q-1,
\qquad
M_t=q-2\quad(t\ne0).
\tag{8}
\]

Let `z_t mod Nq` be the unique CRT lift satisfying

\[
z_t\equiv h\pmod N,
\qquad
z_t\equiv t\pmod q.
\tag{9}
\]

The classical differentiated cotangent multiplication formula is

\[
\boxed{
\sum_{t\in\mathbb F_q}
\frac1{4\sin^2(\pi z_t/(Nq))}
=
q^2\frac1{4\sin^2(\pi h/N)}.
}
\tag{10}
\]

For `t=0`, the lift is divisible by `q`. Write `z_0=qc`; then

\[
c\equiv q^{-1}h\pmod N,
\]

so

\[
\frac1{4\sin^2(\pi z_0/(Nq))}
=
\frac1{4\sin^2(\pi q^{-1}h/N)}.
\tag{11}
\]

Using (8), the complete conductance between the two coarse fibers is therefore

\[
q^2(q-2)\frac1{4\sin^2(\pi h/N)}
+
\frac1{4\sin^2(\pi q^{-1}h/N)}.
\tag{12}
\]

Both sides are Laplacians and have zero row sum, so the off-diagonal identity determines the diagonal as well. Hence the **raw** primitive-shell operators satisfy

\[
\boxed{
R_{N,q}L_{Nq}^{\rm int}R_{N,q}^*
=
q^2(q-2)L_N^{\rm int}
+V_qL_N^{\rm int}V_q^{-1}.
}
\tag{13}
\]

Dividing by `(Nq)^2` and then by the fiber norm `q-1` from (7) gives exactly (3).

This calculation uses the full all-chord primitive operator, not a bounded-radius truncation, the gap-two matching projector, the full regular polygon, or a divisor subgroup. It therefore fills a refinement gap left open by PC-039 and PC-148.

## 2. Squarefree refinement is exactly path independent

Let `m` be squarefree and coprime to `N`. The normalized pullback along

\[
U(Nm)\longrightarrow U(N)
\]

has fiber size `phi(m)` and factors through any ordering of the prime divisors of `m`. For distinct new primes `p,q`, multiplication by `q` on `U(Np)` is compatible with reduction to `U(N)`, so

\[
V_q^{(Np)}J_{N,p}=J_{N,p}V_q^{(N)}.
\tag{14}
\]

Applying (3) recursively therefore gives

\[
\boxed{
J_{N,m}^*A_{Nm}J_{N,m}
=
\left[
\prod_{q\mid m}\mathcal S_q
\right](A_N).
}
\tag{15}
\]

The multiplicative permutations `V_q` on `U(N)` commute, hence so do their adjoint actions and

\[
\boxed{
\mathcal S_p\mathcal S_q
=
\mathcal S_q\mathcal S_p.
}
\tag{16}
\]

In particular the direct `Npq -> N` compression and the two staged routes through `Np` or `Nq` are identical. The full primitive-shell operator therefore acquires no ordered-prime curvature or refinement holonomy under this canonical conditional expectation.

This is structurally parallel to PC-049's cotangent fiber-pushforward theorem, but it is not a restatement of it. Here the operator is the positive inverse-square Hessian/chord Laplacian that underlies PC-128--PC-154, and the differentiated multiplication law produces the different coefficient `q^2(q-2)` in (13).

## 3. Every prime step is invertible on the coarse matrix algebra

For `q>=3`, write

\[
a_q:=\frac{q-2}{q-1},
\qquad
b_q:=\frac1{q^2(q-1)}.
\tag{17}
\]

Since `Ad_{V_q}` has finite order, all of its eigenvalues `omega` lie on the unit circle. Every superoperator eigenvalue of (5) is therefore

\[
a_q+b_q\omega.
\tag{18}
\]

But `a_q>b_q>0`, so none can vanish. Thus `S_q` is invertible for every `q>=3`. The doubling case is even more rigid:

\[
\boxed{
\mathcal S_2=\frac14\operatorname{Ad}_{V_2},
}
\tag{19}
\]

which is again invertible.

Therefore, once the extension prime is known, the fiber-constant compressed matrix contains **exactly the same coarse operator information as `A_N`**, transformed by an explicit invertible map. Fine zero-mean fiber directions have certainly been discarded, but no new coarse degree of freedom is created by the compression itself.

## 4. Character channels are a classical Mertens scalar times a nonzero convergent correction

The finite abelian group `U(N)` diagonalizes every multiplicative permutation. For a character `chi`, let

\[
e_\chi(a)=\varphi(N)^{-1/2}\chi(a),
\]

so that

\[
V_qe_\chi=\overline{\chi(q)}e_\chi.
\tag{20}
\]

On the matrix channel `E_{chi,psi}=|e_chi><e_psi|`, put `eta=chi\overline psi`. Then

\[
\operatorname{Ad}_{V_q}E_{\chi,\psi}
=
\overline{\eta(q)}E_{\chi,\psi},
\]

and (5) has the exact channel multiplier

\[
\boxed{
\mu_q(\eta)
=
\frac{q-2}{q-1}
\left(
1+
\frac{\overline{\eta(q)}}{q^2(q-2)}
\right).
}
\tag{21}
\]

The first factor is precisely the two-point reduced-residue factor already controlling PC-139, PC-144, PC-148, and the prime-pair law of PC-151. Over odd primes up to `x`,

\[
\prod_{3\le q\le x}\frac{q-2}{q-1}
=
2\left(\prod_{q\le x}\left(1-\frac1q\right)\right)
\left(\prod_{3\le q\le x}\left(1-\frac1{(q-1)^2}\right)\right)
\sim
\frac{2C_2e^{-\gamma}}{\log x},
\tag{22}
\]

with `C_2` the twin-prime constant in the convention of PC-151. Omitting the finitely many primes already dividing a fixed base `N` only changes the nonzero constant.

The second factor in (21) cannot supply a hidden zero set. Indeed

\[
\sum_q\frac1{q^2(q-2)}<\infty,
\]

and every local factor has modulus bounded away from zero. Hence

\[
\boxed{
K_{N,\eta}
:=
\prod_{q\nmid N,\ q\ge3}
\left(
1+
\frac{\overline{\eta(q)}}{q^2(q-2)}
\right)
}
\tag{23}
\]

converges absolutely to a finite nonzero value.

Thus, after the natural Mertens rescaling needed to compensate the shrinking fiber-constant channel, the only residual arithmetic is an absolutely convergent fixed character correction. There is no intrinsic complex spectral parameter `s`, no gamma completion, no `s <-> 1-s` involution, and no zero divisor capable of selecting `Re(s)=1/2`. Introducing such a parameter into (23) would be an external analytic wrapper rather than structure forced by the refinement geometry.

## 5. Matched controls and relation to the recent full-chord hierarchy

Several controls make the obstruction sharp.

First, `q=2` gives the pure conjugacy (19), matching the recurring Prime-Circle doubling degeneracy from a different operator-level direction. Second, for a composite squarefree factor `m=pq`, direct refinement is **exactly** the same as either ordered pair of prime refinements by (15)--(16). The apparent distinction between a prime-by-prime history and a composite endpoint is therefore absent in this coarse channel.

Third, the correction in (21) is not merely small numerically: after factoring the classical reduced-residue scalar it differs from the identity by `O(q^{-3})` as a superoperator. The complete prime tower therefore converges in operator norm to an invertible correction on the finite coarse matrix algebra.

Finally, this result is compatible with PC-151--PC-154 rather than contradicting their prime-pair/prime-tuple hierarchy. Those findings analyze arithmetic created by the **within-level primitive restriction** and by fixed-support/all-support spectral observables. Equation (3) says that when the entire fine operator is subsequently projected onto functions constant on reduction fibers, all cross-level information surviving that conditional expectation is only the base operator plus one multiplicative conjugate per new prime. The richer tuple data, if it is to organize coherently across levels, must therefore live in the discarded fiber fluctuations, in observables coupling them to coarse modes, or in nonlinear/growing-support constructions not representable by (5).

## 6. Prior-art and novelty audit

The analytic ingredients are classical. Calogero--Perelomov is already the Prime-Circle anchor for the regular-polygon `csc^2` spectral setting. More directly, Matthias Beck, **Dedekind cotangent sums**, *Acta Arithmetica* 109:2 (2003), 109--130, DOI `10.4064/aa109-2-1`, treats cotangent derivatives and Petersson--Knopp distribution identities in a common finite trigonometric framework; since `csc^2` is the first cotangent derivative up to sign and scale, the multiplication law (10) is squarely classical. L. Alayne Parson, **Dedekind sums and Hecke operators**, *Math. Proc. Cambridge Philos. Soc.* 88:1 (1980), 11--14, DOI `10.1017/S0305004100057315`, is the existing Prime-Circle prior-art boundary for interpreting such commuting scale-distribution laws as a new Hecke mechanism.

PC-010 gives the broader warning that the abstract roots-of-unity power-map semigroup is already the Bost--Connes cyclotomic tower. Equation (15) does use extra Euclidean chord geometry absent from that abstract tower, so PC-010 alone does not imply this result; however, once the chord kernel is fiber-compressed, the surviving scale action again reduces to commuting multiplicative permutations with explicit local coefficients.

A directed search across reduced-residue cosecant-square sums, primitive-root trigonometric matrices, inverse-square chord Laplacians, and Petersson--Knopp/Hecke distribution relations did not locate the exact matrix identity (13) for `U(Nq) -> U(N)`. That absence is not evidence of historical priority, and no theorem-level novelty is claimed. The durable value is the Prime-Circle-specific classification: the canonical cross-level conditional expectation of the **full** primitive-shell chord operator has an explicit, invertible, commuting local form and therefore cannot serve as the missing RH mechanism by itself.

## 7. Boundary and consequence for the research line

The route

\[
\boxed{
\text{full primitive-shell inverse-square operator}
\to
\text{fiber-constant power-map compression}
\to
\text{ordered prime-scale dynamics}
\to
\text{new RH spectrum}
}
\]

is ruled out under the stated hypotheses. This closes a concrete cross-level loophole left after the fixed-level/full-chord hierarchy PC-149--PC-154 and strengthens PC-148 from the gap-two matching skeleton to the complete inverse-square operator **only for the fiber-constant coarse channel**.

The boundary matters. The theorem does **not** classify:

- zero-mean modes inside the `q-1` point reduction fibers or coarse/fiber off-diagonal blocks;
- rectangular operators that retain coarse and fine degrees of freedom simultaneously;
- nonlinear couplings between different fiber sectors;
- repeated-prime local refinement, since (15) is stated for squarefree added scale;
- support size growing together with the conductor in the linked-cluster hierarchy;
- or the global uniformization/monodromy branch.

Any surviving full-chord refinement mechanism must therefore keep information destroyed by the conditional expectation `J^*(.)J`, rather than merely iterate that expectation through the cyclotomic tower.

## 8. Exact audit and falsification tests

The core statement is finite-dimensional and directly falsifiable.

1. For any `q\nmid N`, enumerate the `q-1` primitive lifts of two distinct coarse units and verify the difference multiplicities (8).
2. Verify the cosecant multiplication identity (10) on every nonzero coarse difference.
3. Construct the full primitive-shell Laplacians directly and check (13) entry by entry; the normalized isometric compression must then satisfy (3).
4. For distinct new primes `p,q`, compare direct compression from `Npq` with both staged orders and verify (15)--(16).
5. Diagonalize the multiplicative permutations in the character basis and verify the channel multiplier (21).
6. After factoring `(q-2)/(q-1)`, every local residual factor must be `1+O(q^{-3})` and nonzero. A vanishing local factor, a noncommuting square, or any additional coarse matrix term not expressible through `A_N` and its multiplicative conjugate would refute the classification.
