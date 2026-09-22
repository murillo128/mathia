# MI-097 — Staged residual-divisor coordinates can be pure reparametrization

**Evidence level:** exact synthesis from [MC-470](../../findings/MC-470-empty-vector-residual-is-a-nonnegative-sieve-boundary-count.md) and [MC-471](../../findings/MC-471-empty-vector-base-is-two-sided-sifted-translated-ratio-sum.md) for the empty-vector branch of the concrete staged linear-sieve decomposition.

MC-470 shows that the empty-vector divisor recombination is a nonnegative upper-sieve boundary count `B(y)`. MC-471 then restores the exact translated-character geometry before any further q-vdC interpretation. The branch is

`C_h^(0)(I)=sum_n K_h(n) B(n+h)B(n)`,

with `K_h(n)=chi(n+h) conjugate(chi(n))`, equivalently the character of the translated ratio on its support. Decomposing `B=R_z+E` exposes four rough/boundary channels; the leading rough--rough term is a genuinely two-sided translated pair sieve, with each small prime excluding both residues `0` and `-h`.

The staged coordinate `D_s=h/s` arising after writing `n+h=sj` does not create another source phase. It is only a change of variables inside the same translated-ratio sum. Treating it as an independent oscillatory resource would double-count information that the exact recombination has already identified with one source object.

The live analytic problem is therefore a joint pair-sieve/character-cancellation problem. A one-sided rough-number estimate does not automatically apply to the coefficient `B(n+h)B(n)`, and the positive boundary corrections still require their own quantitative affine incidence control. Any gain from staged coordinates must be shown to survive after the exact variables are recombined; otherwise the only genuine oscillation in the empty-vector branch is the translated character phase itself.

**Boundary.** This does not rule out useful changes of variables for estimating the sum, nor does it say that every staged divisor coordinate is redundant in nonempty components. It says only that in the exact empty-vector branch isolated by MC-471, the residual divisor label is not an additional source-side phase or independent cancellation resource.