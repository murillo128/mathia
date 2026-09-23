# FD-298 — Low-height hard complements are near-capacity equivalent to the block-Mertens field

- **Date:** 2026-09-23
- **Status:** proved exact source/complement identity, fixed-packet near-capacity equivalence, and rigid-regime route closure
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** hard Perron complement / fixed spectral packet / block-Mertens field / cutoff-independent residues / physical divisor replication / near-capacity equivalence / route closure
- **Depends on:** FD-234, FD-261, FD-267, FD-280, FD-297
- **Classification:** `EXACT-DERIVED + RH-CONDITIONAL + SIMPLE-ZERO + FIXED-PACKET-SUBCRITICALITY + CUTOFF-INDEPENDENT-TERM-BOUND + SOURCE-EQUIVALENCE + RIGID-REGIME-CLOSURE`

## Claim

FD-297 reduces the whole low-height zero-safe hard-remainder trajectory, below the aggregate rigidity floor, to one fixed low-height baseline. The remaining question there was whether that fixed baseline can be shown to lie inside the near-capacity repair budget.

For the Mertens hard-Perron decomposition, that baseline is not a genuinely simpler spectral object. Up to a capacity-negligible fixed zero packet and the standard cutoff-independent Perron terms, it is exactly the original divisor-smoothed block-Mertens field of FD-234. Consequently, throughout the FD-297 rigidity regime, **every zero-safe low-height hard complement has the same near-capacity classification as the original block-Mertens source itself**.

Write the exact FD-280 decomposition for the ordinary Mertens source as

\[
M(y)=C(y)+P_T(y)+E_T(y),
\tag{1}
\]

where `C` is independent of the nontrivial-zero cutoff, `P_T` is the hard packet of nontrivial-zero residues with positive ordinate at most `T`, and `E_T` is the exact complementary remainder. Extend the sampled objects at `y=0` by the natural physical convention needed for the first Mertens block.

Define the physical Farey map

\[
(\Phi_N f)(d)
:=
\sum_{q\mid d}
\bigl(f(Nq)-f(N(q-1))\bigr),
\tag{2}
\]

and put

\[
G_N:=\Phi_NM,
\qquad
\mathcal C_N:=\Phi_NC,
\qquad
\mathcal G_{T,N}:=\Phi_NP_T,
\qquad
\mathcal R_{T,N}:=\Phi_NE_T.
\tag{3}
\]

Then linearity gives the exact coordinatewise identity

\[
\boxed{
G_N
=
\mathcal C_N+
\mathcal G_{T,N}+
\mathcal R_{T,N}.
}
\tag{4}
\]

Equivalently,

\[
\boxed{
\mathcal R_{T,N}-G_N
=-\mathcal C_N-\mathcal G_{T,N}.
}
\tag{5}
\]

The first term in (3) is precisely the canonical FD-234 block-Mertens field. If

\[
U_N(q):=M(Nq)-M(N(q-1)),
\tag{6}
\]

then

\[
G_N(d)=\sum_{q\mid d}U_N(q),
\qquad
\widetilde c_N(d)=-\frac12G_N(d),
\tag{7}
\]

where `\widetilde c_N` is the canonical real full-grid repair coefficient.

Now assume RH and simple nontrivial zeros, as in FD-297, and fix `T_bullet>0` independently of `N,x`. The packet `P_{T_bullet}` contains only finitely many critical-line Mellin modes. Hence FD-267 gives

\[
\boxed{
\|\mathcal G_{T_\bullet,N}\|_{1,x}
\ll_{T_\bullet}
N^{1/2}x.
}
\tag{8}
\]

For the standard Mertens hard-Perron normalization, the cutoff-independent package has physical size

\[
\boxed{
\|\mathcal C_N\|_{1,x}
\ll x\log(2x).
}
\tag{9}
\]

This includes the residue at `s=0`, any fixed collection of trivial-zero residues (or the absolutely convergent full trivial-zero tail), and the bounded integer-endpoint correction if ordinary rather than half-weighted Mertens values are used.

Combining (5), (8), and (9),

\[
\boxed{
\|\mathcal R_{T_\bullet,N}-G_N\|_{1,x}
\ll_{T_\bullet}
N^{1/2}x+x\log(2x).
}
\tag{10}
\]

Let

\[
\beta:=\log_2\frac32,
\qquad
c:=1-\beta=0.4150374992\ldots,
\tag{11}
\]

and use the FD-297 near-capacity budget

\[
B_{N,x}
:=
\frac{N^{1/2}x^{1+c}}{\ell(x)},
\qquad
\ell(x)\to\infty,
\qquad
\ell(x)=x^{o(1)}.
\tag{12}
\]

In every fixed polynomial-depth regime

\[
x=N^{\lambda+o(1)},\qquad \lambda>0,
\tag{13}
\]

equation (10) yields

\[
\boxed{
\frac{\|\mathcal R_{T_\bullet,N}-G_N\|_{1,x}}
{B_{N,x}}
=
x^{-c+o(1)}
\longrightarrow0.
}
\tag{14}
\]

Consequently

\[
\boxed{
\left|
\frac{\|\mathcal R_{T_\bullet,N}\|_{1,x}}{B_{N,x}}
-
\frac{\|G_N\|_{1,x}}{B_{N,x}}
\right|
=o(1).
}
\tag{15}
\]

This already answers the fixed-anchor question in structural form: estimating the fixed hard remainder at near-capacity scale is asymptotically the same task as estimating the original block-Mertens field.

The conclusion strengthens when combined with FD-297. Let

\[
H=x^{\tau+o(1)}
\tag{16}
\]

and assume the global complete-cluster background hypothesis there, together with

\[
\Delta(\tau,\lambda,b)
=
c-b-\tau-
\frac{\tau}
{2\left(1-\dfrac{\tau}{\pi(1+1/\lambda)}\right)}
>0.
\tag{17}
\]

Then FD-297 gives

\[
\sup_{T\in\mathcal S_L([T_\bullet,H])}
\|\mathcal R_{T,N}-\mathcal R_{T_\bullet,N}\|_{1,x}
=o(B_{N,x}).
\tag{18}
\]

Using (10),

\[
\boxed{
\sup_{T\in\mathcal S_L([T_\bullet,H])}
\frac{\|\mathcal R_{T,N}-G_N\|_{1,x}}
{B_{N,x}}
\longrightarrow0.
}
\tag{19}
\]

Thus below the aggregate rigidity floor the entire zero-safe hard-complement path is **near-capacity equivalent to the original Mertens source field**. Moving the hard cutoff through that regime cannot turn the physical source into an asymptotically easier remainder.

In particular, for every fixed `epsilon>0`, equations (15) and (19) imply:

- if
  \[
  \|G_N\|_{1,x}
  \le(1-\varepsilon)B_{N,x},
  \tag{20}
  \]
  then every zero-safe hard cutoff in the FD-297 rigidity regime is `B_{N,x}`-good for all sufficiently large `x`;

- if
  \[
  \|G_N\|_{1,x}
  \ge(1+\varepsilon)B_{N,x},
  \tag{21}
  \]
  then no such cutoff is `B_{N,x}`-good for all sufficiently large `x`.

Only the `o(B_{N,x})` transition layer remains undecided.

Because of (7), the baseline question is equivalently a direct `l^1` question for the canonical real Mertens repair,

\[
\boxed{
\sum_{x<d\le2x}|\widetilde c_N(d)|
\stackrel{?}{\ll}
\frac12 B_{N,x},
}
\tag{22}
\]

up to `o(B_{N,x})`. This is a source-side problem, not a residual benefit supplied by low-height spectral truncation.

## 1. Exact source/complement bookkeeping

Equation (4) is simply (1) after applying the linear map `\Phi_N`. It is worth isolating because it distinguishes two notions that can otherwise be conflated.

The **total non-packet complement** is

\[
\widehat E_T:=C+E_T=M-P_T.
\tag{23}
\]

Its physical image satisfies the representation-independent identity

\[
\boxed{
\Phi_N\widehat E_T
=G_N-\mathcal G_{T,N}.
}
\tag{24}
\]

No choice of how cutoff-independent contour terms are split between `C` and `E_T` can change (24). At a fixed height, the only spectral difference between the total hard complement and the exact source is therefore the finite admitted zero packet.

If one chooses a fixed anchor strictly below the first positive nontrivial-zero ordinate, then `P_{T_bullet}=0` and (24) becomes the exact identity

\[
\boxed{
\Phi_N\widehat E_{T_\bullet}=G_N.
}
\tag{25}
\]

So at sufficiently low fixed height the total hard complement is not merely close to the block-Mertens field: it **is** the block-Mertens field. Anchors above finitely many zeros differ only by the finite packet in (24).

FD-297 works with `E_T` rather than `C+E_T`, so to transfer this representation-independent statement to its precise baseline one must also control `\Phi_NC`. Equation (9) supplies exactly that control for the standard Mertens Perron architecture.

## 2. A fixed nontrivial-zero packet is subcritical by one full depth power gap

At fixed `T_bullet`, the packet contains finitely many terms of the form

\[
a_\rho y^\rho,
\qquad
 a_\rho=\frac1{\rho\zeta'(\rho)},
\tag{26}
\]

with the usual conjugate pairing when a real-valued packet is desired. Under RH,

\[
\Re\rho=\frac12.
\tag{27}
\]

The weighted packet complexity

\[
W_{T_\bullet}
:=
\sum_{0<\gamma\le T_\bullet}
|a_\rho|(1+|\rho|)
\tag{28}
\]

is therefore a fixed constant independent of `N,x`. FD-267 applies directly and gives

\[
\sum_{x<d\le2x}
|\mathcal G_{T_\bullet,N}(d)|
\ll
W_{T_\bullet}N^{1/2}x,
\tag{29}
\]

which is (8).

Against (12),

\[
\frac{N^{1/2}x}{B_{N,x}}
=
\ell(x)x^{-c}
=x^{-c+o(1)}.
\tag{30}
\]

Thus no **fixed** collection of nontrivial-zero residues can change the near-capacity classification. This is the same linear-depth ceiling already identified in FD-267, now applied to the fixed-anchor remainder question of FD-297.

The conclusion is insensitive to the numerical size of the first few coefficients `1/(rho zeta'(rho))`: they may be large constants, but they do not grow with the Farey depth parameter. Only a packet whose weighted complexity grows polynomially with `x` can compete at the capacity scale.

## 3. Standard cutoff-independent Perron terms are physically negligible

For completeness, consider the usual cutoff-independent residues in the Mertens Perron formula. The pole of the integrand

\[
\frac{y^s}{s\zeta(s)}
\tag{31}
\]

at `s=0` contributes the constant `-2`. Crossing trivial zeros at `s=-2n` contributes terms

\[
a_n y^{-2n},
\qquad
 a_n
=
\frac{(-1)^{n-1}(2\pi)^{2n}}
{(2n)!\,n\,\zeta(2n+1)}.
\tag{32}
\]

A finite leftward contour shift includes only finitely many such terms. If instead the whole trivial-zero tail is packaged into `C`, the series and its derivative converge absolutely and uniformly for `y>=2` because of the factorial in (32). Hence for some absolute constant `K`,

\[
\left|
\sum_{n\ge1}a_n y^{-2n}
\right|
\le K,
\qquad
\left|
\frac d{dy}
\sum_{n\ge1}a_n y^{-2n}
\right|
\le Ky^{-3}
\quad(y\ge2).
\tag{33}
\]

The constant `-2` disappears from every block difference except the first sampled block. Its total replicated contribution on `x<d<=2x` is therefore `O(x)`.

For the trivial-zero tail, the first block again contributes `O(1)` to each depth coordinate. For `q>=2`, the mean-value theorem and (33) give

\[
|C_{\rm triv}(Nq)-C_{\rm triv}(N(q-1))|
\ll
N^{-2}(q-1)^{-3}.
\tag{34}
\]

Using the exact replication multiplicity

\[
m_x(q)
:=
\#\{d:x<d\le2x,\ q\mid d\},
\tag{35}
\]

with `m_x(q)<=2x/q` for `q<=x` and `m_x(q)<=1` for `x<q<=2x`, summing (34) gives only `O(x)` total physical mass.

Finally, passing from half-weighted Perron values at integral endpoints to the ordinary step value `M(y)` introduces at most a bounded correction at each sampled point. If `h(y)=O(1)` denotes any such endpoint convention, then

\[
|h(Nq)-h(N(q-1))|=O(1),
\tag{36}
\]

so

\[
\begin{aligned}
\|\Phi_Nh\|_{1,x}
&\ll
\sum_{q\le2x}m_x(q)\\
&=
\sum_{x<d\le2x}\tau(d)\\
&\ll x\log(2x).
\end{aligned}
\tag{37}
\]

Equations (33)--(37) prove (9) for the standard cutoff-independent package. The logarithm in (9) is only needed to allow an arbitrary bounded endpoint convention; the analytic residue terms themselves cost `O(x)`.

This argument also shows that the result is robust under any fixed finite regrouping of the `s=0`, trivial-zero, and endpoint terms between `C` and `E_T`: every such regrouping changes the physical baseline by `o(B_{N,x})`.

## 4. Rigidity removes the remaining low-height spectral freedom

At one fixed anchor, equations (10)--(15) already say that the hard remainder and the block-Mertens field have the same capacity-scale norm classification. FD-297 then controls the motion away from that anchor.

Indeed, for every zero-safe `T<=H` in the rigidity regime,

\[
\begin{aligned}
\|\mathcal R_{T,N}-G_N\|_{1,x}
&\le
\|\mathcal R_{T,N}-\mathcal R_{T_\bullet,N}\|_{1,x}\\
&\quad+
\|\mathcal R_{T_\bullet,N}-G_N\|_{1,x}.
\end{aligned}
\tag{38}
\]

The first term is `o(B_{N,x})` by FD-297 when `Delta>0`; the second is `o(B_{N,x})` by (14). This proves (19).

For tame complete-cluster backgrounds `b=0`, the numerical range is therefore exactly the FD-297 range: at least

\[
\tau<0.2683381468\ldots
\tag{39}
\]

uniformly in `lambda>0`, and at balanced depth `lambda=1`,

\[
\tau<0.2725714440\ldots .
\tag{40}
\]

Within this range the hard cutoff is spectrally active only at a scale that is invisible to the near-capacity norm. The entire family `\mathcal R_{T,N}` collapses, at that scale, to the single arithmetic field `G_N`.

This does not say that the hard remainder is pointwise close to `M(y)`, nor that individual contour pieces are small. It is a statement after the exact Farey sampling-and-divisor map and in the physical dyadic `l^1` norm relevant to the repair budget.

## 5. Adversarial checks and limits

**Cutoff-independent bookkeeping cannot be ignored arbitrarily.** The exact invariant statement is (24), involving `C+E_T`. To identify `E_T` alone with `M` one needs a physical bound on `C`. Equation (9) verifies that bound for the standard Mertens Perron terms; the finding does not claim it for an artificially chosen cutoff-independent term of capacity-scale size.

**The first sampled block is not hidden.** Negative-power trivial-zero terms are singular at `y=0` if read literally. The proof never evaluates their analytic formula there. The `q=1` sampled contribution is handled separately and is `O(1)` per depth coordinate, hence `O(x)` on the dyadic band. All derivative estimates begin at `q>=2`, where both sampled arguments are at least `N>=2`.

**Endpoint conventions do not change the exponent.** Ordinary Mertens values and Perron half-weights can differ at integer endpoints. Treating the discrepancy only as a bounded sequence gives the deliberately crude `O(x log x)` bound (37), still polynomially below capacity.

**Fixed packet means fixed in the asymptotic family.** Equation (8) fails as a fixed-constant statement if `T_bullet` grows with `x`. Growing spectral complexity is exactly the mechanism quantified in FD-267 and later complete-cluster ledgers. The present reduction concerns the fixed anchor required by FD-297.

**RH and simplicity are inherited, not newly introduced.** They are used to place the fixed packet on the critical line and to remain inside the FD-297 cluster framework. The exact identities (4), (5), and (24) themselves need neither assumption.

**The result does not prove that `G_N` is good or bad.** It removes the idea that the low-height hard remainder is analytically easier merely because a finite set of zero residues has been separated. The source-side norm in (22) remains to be estimated.

**`l^1` goodness is stronger than the original one-sided positivity objective.** FD-234 identifies `G_N` with the canonical real repair up to the factor `-2`. A bound on `\|G_N\|_1` controls both signs, whereas the physical positivity problem ultimately cares about one-sided negative demand and available positive capacity. Therefore failure to prove (22) would not by itself rule out a more sign-sensitive Farey argument; it would rule out this absolute hard-remainder certificate as a simplification.

**No contradiction with high-height Perron estimates.** FD-281 studies the pre-shift truncated-Perron error and shows that classical pointwise control becomes useful only at much greater spectral height. FD-298 concerns the exact post-shift hard complement and only the low-height rigidity regime. At larger `T`, a growing zero packet can have capacity-scale complexity and the equivalence (19) need not hold.

## 6. Prior-art and novelty audit

The ingredients on the classical analytic side are standard: Perron's formula for `1/zeta(s)`, the residue `y^rho/(rho zeta'(rho))` at a simple nontrivial zero, the residue `-2` at `s=0`, and the trivial-zero residues in (32). A fresh literature search checked explicit Mertens formulas, finite sums over nontrivial zeros, truncated Perron representations, and current Mertens remainder estimates. It found the standard contour/residue architecture and modern comparisons of `M(x)` with short zero sums, including the Lee--Leong source already anchored in `SOURCES.md`, but no theorem about the present divisor-replicated Farey near-capacity equivalence.

No literature novelty claim is made for the explicit formula. The substantive content is the line-local combination of the exact FD-280 complement identity, the FD-234 physical block-Mertens inverse, the FD-267 finite-packet depth ceiling, and the FD-297 global low-height rigidity estimate.

No new external theorem is load-bearing, so `SOURCES.md` requires no new anchor.

The result is analytic and conditional in its rigid-regime form. It is not a formalization candidate in its present state.

## Conclusion

FD-297 made the low-height hard-remainder problem static by reducing every zero-safe cutoff below the aggregate rigidity floor to one fixed baseline. FD-298 identifies that baseline: at the near-capacity physical scale, it is the original divisor-smoothed block-Mertens field, up to a fixed zero packet and standard cutoff-independent Perron terms that are smaller by the power `x^c`.

Hence the whole zero-safe low-height hard-complement path satisfies

\[
\mathcal R_{T,N}
=
G_N+o_{\ell^1(I_x)}(B_{N,x})
\]

uniformly throughout the FD-297 rigidity regime. There is no independent low-height spectral remainder theorem left to prove there. The decisive question is source-side:

\[
\|G_N\|_{1,x}
=
2\sum_{x<d\le2x}|\widetilde c_N(d)|
\stackrel{?}{\ll}
\frac{N^{1/2}x^{2-\beta}}{\ell(x)}.
\]

If that absolute source bound is too strong, the next viable route must exploit the **one-sided sign geometry** of the canonical block-Mertens repair rather than expect a low hard zero cutoff to make the complementary remainder smaller.