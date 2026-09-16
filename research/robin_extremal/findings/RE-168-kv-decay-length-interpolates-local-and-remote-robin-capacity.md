# RE-168 — KV decay length interpolates local and remote Robin capacity

**Status:** `EXACT-DERIVED + VARIABLE-SHELL-CAPACITY + GENERALIZED-RELOCATION-SHARPNESS + LOCAL-REMOTE-INTERPOLATION + PRIOR-ART-BOUNDED`.

**Parent findings:** RE-153, RE-154, RE-164, RE-165, RE-166, RE-167.

`RE-167` separates two sharp quantitative-PNT capacities: a fixed multiplicative shell sees

\[
\mathfrak L_b(p,T)
=
\sqrt p\log p\,\frac{e^{-bV(T)}}{\log T},
\]

whereas a full remote tail sees

\[
\mathfrak K_b(p,T)
=
\sqrt p\log p\,\frac{e^{-bV(T)}}{V(T)},
\qquad
V(T)=\frac{(\log T)^{3/5}}{(\log\log T)^{1/5}}.
\]

The apparent local/remote dichotomy is actually a one-parameter interpolation. The intrinsic logarithmic decay length of the Korobov--Vinogradov envelope is

\[
\boxed{
\ell_{\rm KV}(T):=\frac{\log T}{V(T)}.
}
\tag{1}
\]

For a logarithmic shell `[T,Te^W]`, `W=o(\log T)`, define

\[
\boxed{
\mathfrak S_b(p;T,W)
:=
\sqrt p\log p
\int_T^{Te^W}
\frac{e^{-bV(t)}}{t\log t}\,dt.
}
\tag{2}
\]

If two matched sources differ only inside that shell and satisfy the same KV envelope as in `RE-164`--`RE-167`, then their normalized Robin coordinates differ by `O(\mathfrak S_b)`. Against generalized-prime controls this scale is attainable up to fixed constants by concatenating mass-balanced shell relocations.

More sharply, if

\[
\xi_p:=\frac{W}{\ell_{\rm KV}(T)}
=\frac{WV(T)}{\log T}
\longrightarrow \xi\in[0,\infty),
\]

then

\[
\boxed{
\frac{\mathfrak S_b(p;T,W)}{\mathfrak K_b(p,T)}
\longrightarrow
\Phi_b(\xi)
:=
\frac{5}{3b}\left(1-e^{-3b\xi/5}\right).
}
\tag{3}
\]

Consequently fixed-width shells recover `RE-167`, while a shell only `O(\ell_{\rm KV})` wide already has the **same asymptotic capacity scale as the full remote tail**. In fact essentially all remote capacity can be packed inside a subpower shell `T^{1+o(1)}`.

## 1. Variable-shell upper capacity

Retain the normalized source coordinate and the exact matched-source identity from `RE-164` and `RE-167`. If `Q_1,Q_2` agree outside `[T,Te^W]` and

\[
|\vartheta_{Q_i}(t)-t|\le C_i t e^{-bV(t)},
\tag{4}
\]

then

\[
\mathcal A_p(Q_1)-\mathcal A_p(Q_2)
=
\frac{\sqrt p\log p}{Z_p}
\int_T^{Te^W}
(\vartheta_{Q_2}(t)-\vartheta_{Q_1}(t))(-h'(t))\,dt,
\qquad Z_p=2+o(1).
\tag{5}
\]

Since

\[
-h'(t)\ll \frac1{t^2\log t},
\tag{6}
\]

we obtain

\[
\boxed{
|\mathcal A_p(Q_1)-\mathcal A_p(Q_2)|
\ll
\mathfrak S_b(p;T,W).
}
\tag{7}
\]

Thus `\mathfrak S_b` is the natural capacity of a variable-width shell, rather than `W\mathfrak L_b` once the shell becomes long enough for the KV envelope itself to decay appreciably.

## 2. The KV decay profile

Put

\[
y=\log T,
\qquad
v=V(T)=y^{3/5}(\log y)^{-1/5}.
\tag{8}
\]

In logarithmic height `u=\log t`,

\[
\frac{d}{du}V(e^u)
=
\left(\frac35-\frac{1}{5\log u}\right)
\frac{V(e^u)}u.
\tag{9}
\]

Hence on the scale

\[
u=y+s\frac yv,
\tag{10}
\]

with bounded `s`, Taylor expansion gives uniformly

\[
V(e^u)=v+\frac35s+o(1),
\qquad
\frac{du}{u}=(1+o(1))\frac{ds}{v}.
\tag{11}
\]

Using (2), if `Wv/y\to\xi<\infty`, then

\[
\begin{aligned}
\mathfrak S_b(p;T,W)
&=(1+o(1))
\sqrt p\log p\,
\frac{e^{-bv}}v
\int_0^\xi e^{-3bs/5}\,ds\\
&=(1+o(1))
\mathfrak K_b(p,T)
\frac{5}{3b}
\left(1-e^{-3b\xi/5}\right),
\end{aligned}
\tag{12}
\]

which proves (3).

For `\xi\to0`,

\[
\Phi_b(\xi)=\xi+O(\xi^2),
\]

and therefore

\[
\boxed{
W=o(\ell_{\rm KV}(T))
\quad\Longrightarrow\quad
\mathfrak S_b(p;T,W)
\sim W\mathfrak L_b(p,T).
}
\tag{13}
\]

This recovers the fixed multiplicative-width law of `RE-167` by taking `W=\log C`.

At the opposite end, the same Laplace estimate remains valid when `\xi\to\infty` subject to `W=o(y)`, and yields

\[
\boxed{
\mathfrak S_b(p;T,W)
\sim
\frac{5}{3b}\mathfrak K_b(p,T).
}
\tag{14}
\]

Equivalently,

\[
\boxed{
\int_T^\infty
\frac{e^{-bV(t)}}{t\log t}\,dt
\sim
\frac{5}{3b}\frac{e^{-bV(T)}}{V(T)}.
}
\tag{15}
\]

Thus `RE-165`'s remote scale is concentrated within only a few KV decay lengths above `T` in logarithmic height.

## 3. Sharpness by concatenated balanced relocations

The upper scale can be attained by the generalized-prime controls used in `RE-167`. Partition `[T,Te^W]` into fixed logarithmic blocks of width `d>0`. Inside each block perform the mass-balanced relocation of `RE-167`: remove a prescribed small amount of generalized Chebyshev mass from an earlier subinterval and reinsert exactly the same mass in a later subinterval.

Each block has two crucial properties. First, its cumulative Chebyshev discrepancy returns **exactly to zero at the block's upper edge**. Therefore discrepancies from distinct blocks do not accumulate in the pointwise PNT envelope: at any height only the active block contributes. Second, its Robin displacement has a fixed sign and size

\[
\asymp_d
\sqrt p\log p\,
\frac{e^{-bV(T_j)}}{\log T_j},
\tag{16}
\]

where `T_j` is that block's lower edge. Summing (16) over the disjoint blocks is a Riemann sum for (2), so

\[
\boxed{
|\Delta\mathcal A_p|
\asymp_d
\mathfrak S_b(p;T,W)
}
\tag{17}
\]

up to fixed geometry constants, while the source remains in the same KV exponent class.

The ordinary-prime mass available in each fixed-width block is `\asymp T_j`, whereas the relocated mass is only `O(T_j e^{-bV(T_j)})=o(T_j)`. The discretization errors are negligible under the same density condition used in `RE-167`, for example

\[
\frac{T\log T}{\sqrt p\log p}\longrightarrow\infty,
\tag{18}
\]

which holds throughout the moving-height regime relevant to this line. Thus widening the shell does not introduce a hidden cumulative-envelope cost.

This sharpness statement remains a **generalized-source obstruction**, not a theorem that ordinary primes or the CA selector realize the adversarial relocation.

## 4. Remote capacity is already subpower-local

Equation (3) changes the geometric interpretation of the remote obstruction. A shell of exactly `c\ell_{\rm KV}(T)` logarithmic width captures the fraction

\[
1-e^{-3bc/5}
\tag{19}
\]

of the limiting remote envelope integral, after the common factor `5/(3b)` is removed. So the transition from local to remote capacity occurs over only `Theta(\ell_{\rm KV})` in `\log t`.

More strongly, choose any `\omega_T\to\infty` with

\[
\omega_T=o(V(T))
\]

and set

\[
W=\omega_T\ell_{\rm KV}(T).
\tag{20}
\]

Then `W=o(\log T)` and

\[
Te^W
=
T^{1+\omega_T/V(T)}
=
T^{1+o(1)},
\tag{21}
\]

while (14) shows that this subpower shell already captures `1-o(1)` of the full remote capacity. Thus the word *remote* in `RE-165`--`RE-166` should not be read as requiring a genuinely distant power scale: the quantitative-PNT leakage is concentrated just above the lower endpoint on the KV decay-length scale.

This also explains the moving-center gap in `RE-167`. Since

\[
\frac{\mathfrak K_b(p,T)}{\mathfrak L_b(p,T)}
=
\ell_{\rm KV}(T),
\tag{22}
\]

the local-center displacement is the logarithmic price of restricting the available width from `Theta(\ell_{\rm KV})` to `O(1)`. More generally, in the sub-KV regime the condition `\mathfrak S_b\asymp1` differs from remote capacity one by

\[
V(T_*)-V(T_W)
=
\frac1b\log\frac{\ell_{\rm KV}(T_*)}{W}
+o(\log\ell_{\rm KV}(T_*)),
\tag{23}
\]

provided `W` varies slowly enough across the transition window. For fixed `W`, this recovers the `Theta(\log\log p)` separation of `RE-167`; for `W\asymp\ell_{\rm KV}`, only an `O(1)` displacement remains.

## 5. Falsification and scope

Three possible failure modes were checked.

**Accumulation across blocks.** Naively stacking many local perturbations could violate the KV envelope. The exact mass balance in each block prevents this: the cumulative perturbation is reset to zero before the next block starts.

**Insufficient source mass.** A block needs only an `e^{-bV(T_j)}` fraction of its available Chebyshev mass, hence the required relocation remains asymptotically sparse. The generalized-source discretization error is lower order under (18).

**Breakdown of the profile expansion.** For bounded `\xi`, the quadratic Taylor correction to `V` on the scale `y/v` is `O(1/v)`. For `\xi\to\infty`, endpoint Laplace asymptotics give (14) as long as `W=o(y)`. No power-scale uniformity is being claimed beyond that range.

A prior-art search found the expected literature on KV PNT remainders and Beurling/generalized-prime constructions, but no result identifying this Robin shell capacity or the interpolation profile (3). No new external theorem is load-bearing: the only analytic input is the KV envelope already anchored in `SOURCES.md`, together with the matched-source Robin identity and generalized relocation mechanism established in `RE-164`--`RE-167`.

## 6. Consequence for the research frontier

The source-side uncertainty is now parameterized by one dimensionless width,

\[
\boxed{
\xi=\frac{W}{\ell_{\rm KV}(T)}.
}
\tag{24}
\]

Fixed-width shells and full remote tails are not separate mechanisms. They are the `\xi\to0` and `\xi\to\infty` limits of the same capacity law. Quantitative PNT information cannot isolate the selector merely by restricting perturbations to a shell that is subpower in `T`; a shell of width `\omega_T\ell_{\rm KV}(T)` with `\omega_T\to\infty` is still `T^{1+o(1)}` yet has essentially full remote capacity.

Therefore the accepted `clean-peak-selector-height-coupling` clue remains open. The next genuinely new ingredient must constrain **where inside this KV decay-length window the actual CA/ordinary-prime source can move**, rather than only improve the global PNT envelope or distinguish bounded from unbounded multiplicative shells.

**Provenance:** derived against default-branch snapshot `c26cbea165b2301803c92eee282d35e86e42d940`; finding prefix `RE`; no `mind/**`, clue-state, or source-registry mutation required.