# NB-142 — logarithmic confluence cells force order-log zero-count remainder jumps

**Status:** `DERIVED + SOURCE-SPECIFIC + RIEMANN-VON-MANGOLDT-INCREMENT + POLYNOMIAL-WORST-CELL + FUNCTIONAL-EQUATION-SYMMETRY + LINDELOF-CONDITIONAL-EXCLUSION + TARGET-AWARE-CONFLUENCE-BRIDGE + METHOD-BOUNDARY`.

`NB-140` identifies a representation-invariant obstruction: a simple packet of rank `d_G ~ c log G` inside a sufficiently small two-dimensional polynomial cell can have vanishing normalized Nyman-target projection. `NB-141` then shows that Selberg zero density makes such cells power-law rare in height but does not exclude a sparse exceptional sequence.

There is a sharper source interpretation of exactly what an exceptional sequence would cost. Let

\[
M(T):=\frac{T}{2\pi}\log\frac{T}{2\pi e},
\qquad
R(T):=N(T)-M(T),
\tag{1}
\]

where `N(T)` counts nontrivial zeta zeros with `0<Im rho<=T`, with multiplicity, using any standard endpoint convention. The Bellotti--Wong--Fiori estimate already anchored in `SOURCES.md` gives

\[
|R(T)|
\le
0.10076\log T+0.24460\log\log T+8.08344.
\tag{2}
\]

Fix `B>0` and put

\[
h_G:=G^{-B}.
\tag{3}
\]

For every `u,v` with

\[
G/2\le u<v\le 3G,
\qquad
v-u=O(h_G),
\tag{4}
\]

one has the exact increment reduction

\[
\boxed{
N(v)-N(u)
=
R(v)-R(u)+o(1),
}
\tag{5}
\]

uniformly in `u,v`. The reason is simply that

\[
M'(x)=\frac1{2\pi}\log\frac{x}{2\pi},
\tag{6}
\]

so

\[
M(v)-M(u)
=O(h_G\log G)
=o(1).
\tag{7}
\]

Thus at the polynomial confluence scales of `NB-140`, **local zero occupancy is asymptotically the positive increment of the Riemann--von Mangoldt remainder itself**. No global density theorem is needed for this identification.

Now retain the actual-zero cell geometry of `NB-140`--`NB-141`. Fix

\[
0<a<\frac12
\tag{8}
\]

and suppose that for some `t_G in [G,2G]` the cell

\[
\mathcal C_G(t_G)
:=
\left\{
\rho=\beta+i\gamma:
\zeta(\rho)=0,
\left|\beta-\left(\frac12+a\right)\right|\le h_G,
\ |γ-t_G|\le h_G
\right\}
\tag{9}
\]

contains

\[
d_G\ge c\log G
\tag{10}
\]

zeros for some fixed `c>0`, counted with multiplicity. Eventually `h_G<a/2`, so every zero in `(9)` lies strictly to the right of the critical line. Functional-equation symmetry therefore supplies a distinct left-half partner at the same ordinate and with the same multiplicity. Hence a vertical interval of length `O(h_G)` containing the cell contains at least `2d_G` zeta zeros in total.

Combining this with `(5)` gives the quantitative source cost

\[
\boxed{
\sup_{\substack{G/2\le u<v\le3G\\v-u\le4G^{-B}}}
\bigl(R(v)-R(u)\bigr)
\ge
2c\log G-o(\log G).
}
\tag{11}
\]

Consequently,

\[
\boxed{
R(T)=o(\log T)
\quad\Longrightarrow\quad
\sup_{t\in[G,2G]}\#\mathcal C_G(t)=o(\log G)
}
\tag{12}
\]

for every fixed `a>0` and every fixed polynomial exponent `B>0`.

This is exactly the worst-cell source law needed to eliminate the logarithmic-rank matched packets of `NB-140`. In particular, an infinite sequence of actual `NB-140`-type target-poor cells would force order-`log T` positive jumps of the zero-count remainder across intervals whose lengths shrink like a power of `T`.

The classical Backlund formula identifies

\[
R(T)=S(T)+\frac78+O(T^{-1}),
\qquad
S(T):=\frac1\pi\arg\zeta\!\left(\frac12+iT\right),
\tag{13}
\]

up to the usual endpoint convention. Hence `(11)` is equivalently an order-`log G` upward jump of `S` on a polynomially short interval. R. R. Hall records the classical Cramér implication

\[
\text{Lindelöf hypothesis}
\quad\Longrightarrow\quad
S(T)=o(\log T).
\tag{14}
\]

Therefore the Lindelöf hypothesis, already strictly weaker than RH as a zeta-growth statement, is sufficient to exclude the specific logarithmic confluence obstruction isolated by `NB-140`--`NB-141`.

This does **not** prove RH from Lindelöf, nor does it show that every smaller packet is target-bearing. It identifies the exact source resource consumed by the present matched controls: they require order-log local oscillation in the zero-count remainder / zeta argument. The current explicit `O(log T)` zero-count envelope leaves precisely that resource available; any sublogarithmic remainder law would remove it.

## 1. Polynomially short zero counts are remainder increments

Let `h=h_G=G^{-B}`. For `u,v` satisfying `(4)`, the mean-value theorem and `(6)` give

\[
|M(v)-M(u)|
\le
C_B h\log G
\longrightarrow0.
\tag{15}
\]

Since `N=M+R`, equation `(5)` follows immediately. More quantitatively,

\[
\boxed{
N(v)-N(u)
=
R(v)-R(u)
+O_B(G^{-B}\log G).
}
\tag{16}
\]

This is uniform for all windows of polynomially shrinking length in `[G/2,3G]`.

Define the worst vertical occupancy

\[
Q_B(G)
:=
\sup_{t\in[G,2G]}
\#\{\rho:\zeta(\rho)=0,
\ |\operatorname{Im}\rho-t|\le G^{-B}\},
\tag{17}
\]

again with multiplicity. Endpoint ordinates cause no difficulty: enlarge the window by a factor at most two and choose endpoints `u,v` outside the discrete set of zero ordinates. Then every zero counted in `(17)` lies in `(u,v)`, while `v-u\le4G^{-B}`. Conversely every such interval is contained in a comparable centered window. Therefore

\[
\boxed{
Q_B(G)
=
\sup_{\substack{G/2\le u<v\le3G\\v-u\le4G^{-B}}}
\bigl(R(v)-R(u)\bigr)
+o(\log G)
}
\tag{18}
\]

at the only scale relevant here. In particular,

\[
Q_B(G)=o(\log G)
\tag{19}
\]

is equivalent, up to harmless constant enlargement of the window, to a sublogarithmic bound on the positive local increments of `R`.

This formulation is stronger conceptually than saying that a new local zero theorem is needed. The missing theorem can be stated directly as a short-scale modulus-of-upward-oscillation estimate for the already classical zero-count remainder.

## 2. A right-half confluence packet forces twice its rank into the vertical count

Suppose `(9)` contains `d_G` zeros. Since `h_G<a/2` for large `G`, each has

\[
\beta>\frac12.
\tag{20}
\]

For a nontrivial zeta zero `rho=beta+i gamma`, the functional equation and conjugation imply that

\[
1-\overline\rho=(1-\beta)+i\gamma
\tag{21}
\]

is also a zero with the same multiplicity. Because `beta>1/2`, `(21)` is distinct from `rho`. Thus the vertical interval

\[
[t_G-h_G,t_G+h_G]
\tag{22}
\]

contains at least `2d_G` zeros of the full divisor.

Choose non-zero-ordinate endpoints

\[
u_G\in[t_G-2h_G,t_G-h_G),
\qquad
v_G\in(t_G+h_G,t_G+2h_G].
\tag{23}
\]

Then

\[
N(v_G)-N(u_G)\ge2d_G.
\tag{24}
\]

By `(16)`,

\[
R(v_G)-R(u_G)
\ge
2d_G-o(1).
\tag{25}
\]

If `d_G>=c log G`, this proves `(11)`.

There is an equivalent amplitude statement. From

\[
R(v_G)-R(u_G)
\ge2c\log G-o(\log G)
\tag{26}
\]

at least one endpoint must satisfy

\[
\boxed{
|R(u_G)|\ge c\log G-o(\log G)
\quad\text{or}\quad
|R(v_G)|\ge c\log G-o(\log G).
}
\tag{27}
\]

Thus any infinite sequence of logarithmic-rank right-half confluence cells forces

\[
\limsup_{T\to\infty}
\frac{|R(T)|}{\log T}
>0.
\tag{28}
\]

Via `(13)`, the same statement holds for `|S(T)|/log T`.

## 3. The Bellotti--Wong coefficient is exactly why the current matched control still fits

The explicit bound `(2)` gives, for polynomially short `u,v`,

\[
N(v)-N(u)
\le
0.20152\log G
+0.48920\log\log G
+O(1),
\tag{29}
\]

because the smooth main-term increment is `o(1)` and the two endpoint errors may have opposite signs.

A right-half packet of rank `d_G` contributes at least `2d_G` to this total vertical count. Hence `(29)` only forces

\[
d_G
\le
(0.10076+o(1))\log G.
\tag{30}
\]

This recovers the local compatibility threshold already visible in `NB-140`. The more conservative constant `0.05038` used by the explicit infinite synthetic divisor in `NB-141` comes from a different bookkeeping requirement: after adding each symmetric packet to a baseline with `M(T)+O(1)` zeros, the cumulative positive-ordinate excess itself had to remain below the one-sided `0.10076 log T` envelope. That construction pays `2d_G` directly in the remainder and therefore chose `2c<0.10076`.

The distinction matters. Neither number is proposed as an intrinsic zeta threshold. What is intrinsic to the present source budget is the **order**:

\[
O(\log T)
\quad\text{still permits fixed-positive logarithmic packet rank,}
\tag{31}
\]

whereas

\[
\boxed{o(\log T)\quad\text{forbids every fixed-positive logarithmic packet rank.}}
\tag{32}
\]

So the matched controls of `NB-141` are using exactly the leading-order freedom left by the current zero-count theorem, not an unrelated weakness of Selberg density.

## 4. Lindelöf is already strong enough to remove this obstruction

The reduction above is unconditional: it says what any actual crowded packet would force. To place that threshold against classical zeta conjectures, use Backlund's formula `(13)`.

Hall's 1999 paper *On the Zeros of the Riemann Zeta-Function* states the classical bounds

\[
S(T)=O(\log T)
\tag{33}
\]

unconditionally, records Cramér's theorem

\[
\text{Lindelöf}\Longrightarrow S(T)=o(\log T),
\tag{34}
\]

and recalls Littlewood's stronger RH-conditional estimate

\[
S(T)
=O\!\left(\frac{\log T}{\log\log T}\right).
\tag{35}
\]

Reference: R. R. Hall, *On the Zeros of the Riemann Zeta-Function*, Journal of the London Mathematical Society 59 (1999), 65--75, DOI `10.1112/S0024610798006942`.

No novelty is claimed for `(13)`, `(33)`--`(35)`, or their classical relationship to multiplicity and short-interval zero counts. The line-local consequence is the splice with the exact `NB-140` target-poor cell geometry:

\[
\boxed{
\text{Lindelöf}
\Longrightarrow
Q_B(G)=o(\log G)
\Longrightarrow
\text{no logarithmic-rank NB-140 confluence packet.}
}
\tag{36}
\]

This is useful because the source input needed to kill the current obstruction is therefore known to lie **below RH in the classical conjectural hierarchy**. One does not need RH merely to rule out this particular target-poor packet mechanism.

## 5. The truly local hypothesis is weaker than global `S(T)=o(log T)`

For the Nyman application, even `(34)` is more than necessary. By `(18)`, it is enough to prove the one-sided local increment law

\[
\boxed{
\sup_{\substack{G/2\le u<v\le3G\\v-u\le4G^{-B}}}
\bigl(R(v)-R(u)\bigr)
=o(\log G)
}
\tag{37}
\]

for the polynomial exponents `B` entering `NB-140`. Equivalently through Backlund,

\[
\sup_{v-u\le4G^{-B}}
\bigl(S(v)-S(u)\bigr)
=o(\log G).
\tag{38}
\]

This does **not** require a global amplitude estimate `S(T)=o(log T)` if some other source argument can control only short positive increments. It is therefore a more precise next target than asking generically for a stronger zero-density theorem or for Lindelöf itself.

Conversely, every `NB-140`-type actual packet of rank `c log G` violates `(37)` by a fixed proportion. The source question and the target-aware geometric obstruction now meet at a single scalar quantity: the positive polynomial-scale increment of the zero-count remainder.

## 6. Prior-art and novelty boundary

The ingredients external to this line are classical and are not claimed as new:

- the Riemann--von Mangoldt/Backlund decomposition of `N(T)`;
- the explicit Bellotti--Wong--Fiori `O(log T)` error already anchored in `SOURCES.md`;
- Cramér's Lindelöf-conditional `S(T)=o(log T)`, as recorded by Hall;
- Littlewood's stronger RH-conditional bound on `S(T)`.

Hall explicitly motivates `S(T)` through multiplicity and zeros in short intervals, so a generic claim that sublogarithmic `S` limits short-interval multiplicity would be classical. The substantive content here is narrower and line-specific: `NB-140` identifies a precise logarithmic-rank **two-dimensional polynomial cell** whose entire simple-state span is target-poor; `NB-141` shows global zero density cannot exclude a sparse sequence of such cells; the present finding proves that any actual sequence of those cells would necessarily consume order-log local oscillation of the classical zero-count remainder, and that the exact source threshold needed to remove the obstruction is the short-increment law `(37)`.

A literature audit also found modern work on zeros in short regions and recent inverse theorems linking large zeta-type sums to zero concentration, but no unconditional theorem supplying `(37)` uniformly at polynomially shrinking scales. Those neighboring results do not alter the present worst-cell boundary.

## 7. Adversarial audit

Several possible overstatements are worth excluding explicitly.

**This is not a proof that actual zeta zeros satisfy the needed local bound.** Equation `(37)` is precisely the new source information still missing unconditionally.

**Lindelöf is used only as a sufficient classical benchmark.** The finding does not derive Lindelöf from Nyman--Beurling data and does not claim that `(37)` is equivalent to Lindelöf.

**The factor two in `(11)` is legitimate.** The `NB-140` cell lies eventually strictly in `Re s>1/2`; every right-half zero has a distinct functional-equation partner at the same positive ordinate in `Re s<1/2`, with the same multiplicity.

**No simplicity assumption is needed for the zero-count reduction.** `N(T)` counts multiplicity. Simplicity belongs only to the `NB-140` state construction whose obstruction is being tested.

**Endpoint zeros do not create a loophole.** The cell can be enclosed by an interval enlarged by at most a constant factor whose endpoints are not zero ordinates, preserving the polynomial scale and all `o(log G)` conclusions.

**The polynomial scale is essential to the `o(1)` main-term increment.** For `h_G=G^{-B}`, `M(t+h_G)-M(t-h_G)=O(G^{-B}log G)=o(1)`. The statement is not being silently extended to unit-length intervals where the smooth zero density itself contributes `Theta(log G)` zeros.

**Global zero density and short-increment control remain different resources.** `NB-141` already constructs a sparse matched divisor compatible with strong global density but with order-log local remainder jumps. The present finding identifies those jumps rather than contradicting that construction.

## 8. Research consequence

After `NB-141`, the frontier was phrased as a need for either a worst-cell occupancy theorem or a direct target-bearing theorem for crowded actual packets. `NB-142` makes the first option exact:

\[
\boxed{
\text{prove sublogarithmic positive increments of }R(T)
\text{ on the relevant polynomial scales,}
}
\tag{39}
\]

or bypass occupancy altogether with target geometry.

Sharpening a global zero-density exponent still does not address `(39)`. Sharpening the **local oscillation** of the Riemann--von Mangoldt remainder does. The classical Lindelöf implication shows that the required source behavior is analytically coherent and strictly weaker than invoking RH itself, while the Bellotti coefficient and the `NB-141` matched control show why present unconditional counting information stops exactly one order too early.