# FD-255 — Global Möbius rows collapse exact-omission reachability to the sparse double-log scale

- **Date:** 2026-09-21
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** divisor-response sampling / exact omissions / global coefficient envelope / Möbius reachability / incidence-conditioning reconciliation / sublinear-defect coercivity
- **Depends on:** FD-225, FD-244, FD-248, FD-253, FD-254
- **Classification:** `EXACT-DERIVED + SYNTHESIS-CLOSURE + GLOBAL-ROW-REACHABILITY + DOUBLE-LOG-AMPLIFICATION-CEILING + SUBLINEAR-DEFECT-COERCIVITY`

## Claim

FD-248--FD-254 study the inverse seen after restricting the coefficient equations to the active increment support, and most recently to the companion subsystem of a paired exact-omission family. Those restricted matrices can be very ill-conditioned: in the parity-dilation case FD-254 allows a companion inverse norm as large as a power `H^(rho_2-1+epsilon)` with `rho_2-1=0.377785...`.

That polynomial companion conditioning is **not reachable by the full exact-omission inverse under the global coefficient envelope**. The missing compatibility is already implicit in the arithmetic Möbius inversion used in FD-244: every active increment is reconstructed from *all* divisor coefficient rows, not only the active or companion rows.

Let

\[
Y(m)=(\mathscr A b)(m),\qquad Y(0)=0,
\qquad |b_n|\le C_b n\quad(1\le n\le H),
\tag{1}
\]

and suppose the response is exactly zero outside an omission set

\[
E\subseteq\{1,\ldots,H\},
\qquad |E|=K:
\qquad
Y(m)=0\quad(m\notin E).
\tag{2}
\]

Put

\[
g=\mu*b=\Delta Y,
\qquad
D:=\{d\le H:g(d)\ne0\}.
\tag{3}
\]

Then

\[
D\subseteq E\cup((E+1)\cap[1,H]),
\qquad |D|\le2K.
\tag{4}
\]

For `0<delta<=1` define, as in FD-244,

\[
L(\delta):=\log\!\left(e+\log\frac1\delta\right),
\qquad
\Phi(\delta):=\delta L(\delta),
\tag{5}
\]

and put `Phi(0)=0`. Let

\[
\eta:=\min\!\left(1,\frac{2K}{H}\right).
\tag{6}
\]

Then the **full reachable weighted increment mass** satisfies

\[
\boxed{
\sum_{d\in D}\frac{|g(d)|}{d}
\ll
C_b H\Phi(\eta),
}
\tag{7}
\]

and consequently the complete coefficient mass below the horizon obeys

\[
\boxed{
\sum_{n\le H}|b_n|
\ll
C_b H^2\Phi(\eta).
}
\tag{8}
\]

Moreover every individual active coordinate satisfies

\[
\boxed{
\frac{|g(d)|}{d}
\le C_b\sigma_{-1}(d)
\ll C_b\log(e+\log d).
}
\tag{9}
\]

The second inequality follows directly from the FD-244 high-moment estimate and needs no new maximal-order theorem.

Therefore, whenever

\[
K=o(H),
\tag{10}
\]

one has

\[
\boxed{
\frac{\sum_{H/2<n\le H}|b_n|}
     {\sum_{H/2<n\le H}n}
\longrightarrow0.
}
\tag{11}
\]

This conclusion holds for **arbitrary exact omission geometry**, not only pure dilations or isolated omissions. In particular, for `K=H^{alpha+o(1)}` every exponent `alpha<1` is macroscopically coercive, with

\[
\sum_{n\le H}|b_n|
\ll
C_b H^{1+\alpha+o(1)}\log\log H.
\tag{12}
\]

Thus the live polynomial lower-construction question left after FD-254 has a negative answer at the full coefficient level: a polynomially large normalized companion-inverse direction cannot survive the global envelope. The polynomial incidence norms of FD-249--FD-254 remain valid properties of restricted subsystems, but their bad unit-cube directions are not globally extendable coefficient data.

## Global arithmetic Möbius inversion supplies the missing rows

FD-225 gives the exact identities

\[
b=\mathbf1*g,
\qquad
g=\mu*b,
\qquad
g(m)=Y(m)-Y(m-1).
\tag{13}
\]

The active-support inverse of FD-248 evaluates the first identity only at rows `d in D`. If `Z_D` is the induced divisibility zeta matrix, that gives the finite system

\[
\beta_D=W_Dx_D,
\qquad
W_D=R_D^{-1}Z_D R_D,
\tag{14}
\]

whose unrestricted inverse norm is `kappa(D)=||W_D^{-1}||_infinity`. FD-253 makes the analogous restriction to companion rows.

But an actual coefficient sequence satisfying (1) does not supply an arbitrary vector in the active-row unit cube. For every active `d`, the second identity in (13) also gives

\[
 g(d)
 =
 \sum_{q\mid d}\mu(d/q)b_q.
\tag{15}
\]

The sum in (15) uses **every arithmetic divisor row** `q|d`, including rows not belonging to `D` and rows discarded by the companion subsystem. The global envelope therefore implies

\[
\begin{aligned}
|g(d)|
&\le
C_b\sum_{q\mid d}q\\
&=C_b d\sigma_{-1}(d),
\end{aligned}
\tag{16}
\]

which is the first inequality in (9).

This is the extension constraint missing from a large value of `kappa(D)` or `kappa(C)`: the restricted inverse may map some bounded active-row vector to a huge normalized increment, but that active-row vector need not extend to coefficient values on all divisor rows while preserving `|b_q|<=C_bq`.

## FD-244 converts the pointwise extension constraint into a sparse aggregate ceiling

The sharp finite sparse-set estimate of FD-244 states that for every `A subseteq[1,H]` of density `delta=|A|/H`,

\[
\sum_{m\in A}\sigma_{-1}(m)
\ll
H\Phi(\delta),
\tag{17}
\]

with an absolute implied constant. Apply (17) to the actual increment support `D`. Equations (16)--(17) give

\[
\sum_{d\in D}\frac{|g(d)|}{d}
\le
C_b\sum_{d\in D}\sigma_{-1}(d)
\ll
C_bH\Phi(|D|/H).
\tag{18}
\]

By (4), `|D|/H<=eta`; FD-244 also proves that `Phi` is increasing on `[0,1]`. Hence (18) gives (7).

Now reconstruct every coefficient below the horizon from `b=1*g`:

\[
\begin{aligned}
\sum_{n\le H}|b_n|
&\le
\sum_{d\in D}|g(d)|
\left\lfloor\frac Hd\right\rfloor\\
&\le
H\sum_{d\in D}\frac{|g(d)|}{d}.
\end{aligned}
\tag{19}
\]

Substitution of (7) proves (8). This is a total-mass version of the exact-zero consequence latent in the dyadic sampling estimate of FD-244; the important new consequence here is its reconciliation with the later incidence-conditioning branch.

For (9), FD-244 proves uniformly in integers `q>=1` and `N>=1` that

\[
\left(
\frac1N\sum_{n\le N}
\left(\frac n{\varphi(n)}\right)^q
\right)^{1/q}
\ll \log(2q).
\tag{20}
\]

Since `sigma_{-1}(d)<=d/phi(d)`, take `N=d` and `q=ceil(log d)` for `d>=3`. The single `n=d` term in (20) gives

\[
\frac d{\varphi(d)}
\ll
d^{1/q}\log(2q)
\ll
\log(e+\log d),
\tag{21}
\]

and the finitely many small `d` are absorbed into the constant. This proves the second inequality in (9).

## Sublinear exact omissions cannot reach macroscopic coefficient capacity

The dyadic coefficient capacity satisfies

\[
\sum_{H/2<n\le H}n\asymp H^2.
\tag{22}
\]

Because the left side of (11) is bounded by the total mass in (8),

\[
\frac{\sum_{H/2<n\le H}|b_n|}
     {\sum_{H/2<n\le H}n}
\ll
C_b\Phi(\eta).
\tag{23}
\]

If `K=o(H)`, then `eta->0` and

\[
\eta\log\!\left(e+\log\frac1\eta\right)\to0.
\tag{24}
\]

This proves (11).

For the polynomial regime `K=H^{alpha+o(1)}` with fixed `alpha<1`,

\[
\eta=H^{\alpha-1+o(1)},
\qquad
L(\eta)=O(\log\log H),
\tag{25}
\]

so (8) gives (12).

The conclusion is stronger than the pure-dilation window of FD-254. For parity dilation that finding established coercivity from companion-chain entropy only for

\[
\alpha<2-\rho_2
=0.6222148301\ldots .
\tag{26}
\]

Once the full global coefficient rows are restored, (11) extends the macroscopic response-side coercive window to **every `alpha<1`**, independently of `rho_2` and independently of the companion divisibility geometry.

## Why large incidence norms do not contradict the global ceiling

FD-248 gives, from the active rows alone,

\[
\sum_{n\le H}|b_n|
\le
C_bH|D|\kappa(D).
\tag{27}
\]

It follows that macroscopic coefficient mass would require roughly

\[
\kappa(D)\gtrsim H/K.
\tag{28}
\]

FD-249--FD-254 then investigate whether the restricted incidence matrices can develop large enough norms. Those results are correct, but (28) is only a necessary condition extracted from a relaxation. Equation (18) supplies the missing reachability bound for the actual inverse.

Define the realized average normalized amplification

\[
\mathcal A_H(g)
:=
\frac1{C_b|D|}
\sum_{d\in D}\frac{|g(d)|}{d}
\qquad(D\ne\varnothing).
\tag{29}
\]

From (18), with `delta=|D|/H`,

\[
\boxed{
\mathcal A_H(g)
\ll
L(\delta).
}
\tag{30}
\]

If `|D|=o(H)`, then

\[
L(\delta)
=
\log\!\left(e+\log\frac H{|D|}\right)
=
 o\!\left(\frac H{|D|}\right).
\tag{31}
\]

So the amplification scale required by (28) is separated from the actually reachable average amplification by a diverging factor. Even more strongly, (9) prevents any individual normalized increment from carrying a fixed positive power of `H`.

Thus a construction with `kappa(C)=H^beta` for some `beta>0` would still be informative about the **restricted companion matrix**, but it cannot produce `H^beta` normalized increment amplification inside a globally envelope-admissible exact-omission sequence. The bad singular directions live outside the extendable data subspace.

## Finite audit: the FD-254 companion extremizer already violates an omitted row

The small parity example from FD-254 makes the extension failure visible. Take

\[
C=\{3,9,15,45\},
\qquad
E=C-1=\{2,8,14,44\}.
\tag{32}
\]

The companion row at `45` has weighted inverse absolute row sum

\[
1+\frac13+\frac15+\frac1{15}=\frac85.
\tag{33}
\]

Choose companion normalized coefficient data

\[
(\beta_3,\beta_9,\beta_{15},\beta_{45})
=(1,-1,-1,1),
\tag{34}
\]

which aligns all four signs in that inverse row. Solving the companion subsystem gives

\[
(x_3,x_9,x_{15},x_{45})
=\left(1,-\frac43,-\frac65,\frac85\right),
\qquad
x_c=\frac{g(c)}c.
\tag{35}
\]

Pairing forces the start increments to be the opposites of the companion increments. In particular

\[
g(3)=3,
\qquad
g(45)=72,
\qquad
g(2)=-3,
\qquad
g(44)=-72.
\tag{36}
\]

The companion rows themselves all satisfy `|b_c|/c=1` by construction. But the discarded start-side coefficient row at `44` is

\[
b_{44}=g(2)+g(44)=-75,
\qquad
\frac{|b_{44}|}{44}=rac{75}{44}>1.
\tag{37}
\]

So the unit-cube companion extremizer does **not** extend to a global coefficient sequence with `C_b=1`. This finite example is not used in the proof of (7)--(11); it simply exhibits, in the same support used by FD-254, the compatibility mechanism quantified globally by (16)--(18).

## Prior-art / novelty audit

Arithmetic Möbius inversion, incidence-algebra inversion and qualitative uncertainty principles for Möbius pairs are classical. Targeted prior-art searches found, in particular, Pollack--Sanna's uncertainty principles for arithmetic Möbius pairs and Goh's poset generalization. Those results concern support incompatibility and related qualitative questions; they do not supply the finite weighted coefficient-envelope estimate (7)--(9) used here.

No external theorem is newly load-bearing. The only nontrivial quantitative input, the sparse reciprocal-divisor estimate (17) and its high-moment form (20), is already proved and source-anchored in FD-244. Equations (13)--(19) are exact internal divisor algebra. Therefore this pass adds no dependency to `SOURCES.md` and makes no novelty claim for Möbius inversion or sparse-divisor distribution themselves.

The new line-level conclusion is the reconciliation that became necessary only after FD-248--FD-254: **restricted incidence conditioning is not the reachability norm of the full exact-omission problem**. The global coefficient rows collapse every sublinear exact-omission family back to the FD-244 sparse double-log scale.

## Boundary and research consequence

This is still a signed response-space theorem. It does not impose positivity, finite prime-reservoir capacity, squarefree source realization or arithmetic coherence of a physical Farey source. It also does not prove that the upper factor `L(delta)` is sharp for the fully realizable exact-omission map; FD-244 proves sharpness for the sparse arithmetic weight, not simultaneous saturation of every coefficient constraint.

What it does close is the **macroscopic response-side exact-zero branch for sublinear omissions**. Searching for a polynomial lower bound in the companion or active-support inverse cannot reopen that branch, because the full coefficient extension already limits realized normalized increments to double-logarithmic scale.

A remaining exact-zero response question can still ask for the true finer-than-capacity norm: can the factor

\[
L(\delta)=\log\!\left(e+\log\frac1\delta\right)
\]

be reduced, perhaps all the way to a constant, once exact paired geometry is imposed? FD-245 proves that it disappears when the omission count is fixed, so there is still a genuine quantitative problem when `K->infinity`. But that question is now explicitly **below macroscopic capacity**.

The independent source-side problem remains unchanged: after response-space coercivity has excluded sublinear exact-zero hiding, determine what positivity, reservoir capacity, squarefree realization and arithmetic coherence do in the regimes not covered by this sampling theorem.

## Status

**Proved.** The pointwise reachability bound (9), sparse aggregate bound (7), total coefficient-mass estimate (8), and sublinear-defect coercivity (11) follow from exact Möbius inversion plus FD-244. The finite FD-254 audit confirms concretely that a restricted companion extremizer can violate a global coefficient row. The result closes the polynomial full-paired-inverse escape at macroscopic coefficient scale; it does not claim sharpness of the residual double-log factor for realizable exact-omission families and does not imply RH.
